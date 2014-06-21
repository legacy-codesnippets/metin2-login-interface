import dbg
import app
import net
import AvenueOkay
import ime
import snd
import wndMgr
import musicInfo
import serverInfo
import systemSetting
import ServerStateChecker
import locale
import constInfo
import uiCommon
import time
import ServerCommandParser
import ime
import uiScriptLocale
import chat
import sys
import os
import md5
import s_info
#import urllib
import string
#from urllib import FancyURLopener

RUNUP_MATRIX_AUTH = FALSE
NEWCIBN_PASSPOD_AUTH = FALSE

LOGIN_DELAY_SEC = 0.0
SKIP_LOGIN_PHASE = FALSE
SKIP_LOGIN_PHASE_SUPPORT_CHANNEL = FALSE
FULL_BACK_IMAGE = TRUE

PASSPOD_MSG_DICT = {}

VIRTUAL_KEYBOARD_NUM_KEYS = 46
VIRTUAL_KEYBOARD_RAND_KEY = FALSE

ausgefahren = 0
arbeitet = 0
AKTCHANNEL = 0

def Suffle(src):
	if VIRTUAL_KEYBOARD_RAND_KEY:
		items = [item for item in src]

		itemCount = len(items)
		for oldPos in xrange(itemCount):
			newPos = app.GetRandom(0, itemCount-1)
			items[newPos], items[oldPos] = items[oldPos], items[newPos]

		return "".join(items)
	else:
		return src

if locale.IsNEWCIBN() or locale.IsCIBN10():
	LOGIN_DELAY_SEC = 20.0
	FULL_BACK_IMAGE = TRUE
	NEWCIBN_PASSPOD_AUTH = TRUE
	PASSPOD_MSG_DICT = {
		"PASERR1"	: locale.LOGIN_FAILURE_PASERR1,
		"PASERR2"	: locale.LOGIN_FAILURE_PASERR2,
		"PASERR3"	: locale.LOGIN_FAILURE_PASERR3,
		"PASERR4"	: locale.LOGIN_FAILURE_PASERR4,
		"PASERR5"	: locale.LOGIN_FAILURE_PASERR5,
	}

elif locale.IsYMIR() or locale.IsCHEONMA():
	FULL_BACK_IMAGE = TRUE

elif locale.IsHONGKONG():
	FULL_BACK_IMAGE = TRUE
	RUNUP_MATRIX_AUTH = TRUE 
	PASSPOD_MSG_DICT = {
		"NOTELE"	: locale.LOGIN_FAILURE_NOTELEBLOCK,
	}

elif locale.IsJAPAN():
	FULL_BACK_IMAGE = TRUE

def IsFullBackImage():
	global FULL_BACK_IMAGE
	return FULL_BACK_IMAGE

def IsLoginDelay():
	global LOGIN_DELAY_SEC
	if LOGIN_DELAY_SEC > 0.0:
		return TRUE
	else:
		return FALSE

def IsRunupMatrixAuth():
	global RUNUP_MATRIX_AUTH
	return RUNUP_MATRIX_AUTH	

def IsNEWCIBNPassPodAuth():
	global NEWCIBN_PASSPOD_AUTH
	return NEWCIBN_PASSPOD_AUTH

def GetLoginDelay():
	global LOGIN_DELAY_SEC
	return LOGIN_DELAY_SEC

app.SetGuildMarkPath("test")

class ConnectingDialog(AvenueOkay.ScriptWindow):

	def __init__(self):
		AvenueOkay.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		AvenueOkay.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = AvenueOkay.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/ConnectingDialog.py")

			self.board = self.GetChild("board")
			self.message = self.GetChild("message")
			self.countdownMessage = self.GetChild("countdown_message")

		except:
			import exception
			exception.Abort("ConnectingDialog.LoadDialog.BindObject")

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Lock()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()		

	def Close(self):
		self.Unlock()
		self.Hide()

	def Destroy(self):
		self.Hide()
		self.ClearDictionary()

	def SetText(self, text):
		self.message.SetText(text)

	def SetCountDownMessage(self, waitTime):
		self.countdownMessage.SetText("%.0f%s" % (waitTime, locale.SECOND))

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = AvenueOkay.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = AvenueOkay.__mem_func__(event)

	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			self.SetCountDownMessage(self.endTime - time.clock())

	def OnPressExitKey(self):
		#self.eventExit()
		return TRUE

class LoginWindow(AvenueOkay.ScriptWindow):

	IS_TEST = net.IsTest()

	def __init__(self, stream):
		print "NEW LOGIN WINDOW  ----------------------------------------------------------------------------"
		AvenueOkay.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.matrixInputChanceCount = 0
		self.lastLoginTime = 0
		self.inputDialog = None
		self.connectingDialog = None
		self.stream=stream
		self.isNowCountDown=FALSE
		self.isStartError=FALSE

		self.xServerBoard = 0
		self.yServerBoard = 0
		
		self.loadingImage = None

		self.virtualKeyboard = None
		self.virtualKeyboardMode = "ALPHABET"
		self.virtualKeyboardIsUpper = FALSE
		
	def __del__(self):
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)
		AvenueOkay.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE LOGIN WINDOW"

	def Open(self):
		ServerStateChecker.Create(self)

		print "LOGIN WINDOW OPEN ----------------------------------------------------------------------------"

		self.loginFailureMsgDict={
			#"DEFAULT" : locale.LOGIN_FAILURE_UNKNOWN,

			"ALREADY"	: locale.LOGIN_FAILURE_ALREAY,
			"NOID"		: locale.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: locale.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: locale.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: locale.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: locale.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: locale.LOGIN_FAILURE_BLOCK_ID,
			"WRONGMAT"	: locale.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: locale.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: locale.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: locale.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: locale.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: locale.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: locale.LOGIN_FAILURE_WEB_BLOCK,
			
			"HACK"		: "Du wurdest wegen hacken gesperrt.",
			"BOT"		: "Du wurdest wegen benutzung von Bots gesperrt.",
			"SCAM"		: "Du wurdest wegen Betrug gesperrt.",
			"INSULT"	: "Du wurdest wegen Beleidigung gesperrt.",
			"FAKE"		: "Du wurdest aufgrund deiner Namensgebung gesperrt.",
			"NAME"		: "Du wurdest aufgrund deiner Namensgebung gesperrt.",
			"BUG"		: "Du wurdest wegen Bugusing gesperrt.",
			"DK"		: "Du wurdest wegen Dauerkill gesperrt.",
			"OTHER"		: "Du wurdest von der Serverleitung gesperrt.",
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: self.__DisconnectAndInputPassword,
			"WRONGMAT"	: self.__DisconnectAndInputMatrix,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")

		if not self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "LoginWindow.py"):
			dbg.TraceError("LoginWindow.Open - __LoadScript Error")
			return
		
		self.__LoadLoginInfo("loginInfo.py")
		
		if app.loggined:
			self.loginFailureFuncDict = {
			"WRONGPWD"	: app.Exit,
			"WRONGMAT"	: app.Exit,
			"QUIT"		: app.Exit,
			}

		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/"+musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		# pevent key "[" "]"
		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
			
		self.Show()

		global SKIP_LOGIN_PHASE
		if SKIP_LOGIN_PHASE:
			if self.isStartError:
				self.connectBoard.Hide()
				self.loginBoard.Hide()
				self.serverBoard.Hide()
				self.PopupNotifyMessage(locale.LOGIN_CONNECT_FAILURE, self.__ExitGame)
				return

			if self.loginInfo:
				self.serverBoard.Hide()
			else:
				self.__RefreshServerList()
				self.__OpenServerBoard()
		else:
			connectingIP = self.stream.GetConnectAddr()
			if connectingIP:
				self.__OpenLoginBoard()
				if IsFullBackImage():
					self.GetChild("bg1").Show()
					self.GetChild("bg2").Hide()

			else:
				self.__RefreshServerList()
				self.__OpenServerBoard()

		app.ShowCursor()

		self.registerBoard.Hide()
		self.questionBoard.Hide()
	def Close(self):

		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		ServerStateChecker.Destroy(self)

		print "---------------------------------------------------------------------------- CLOSE LOGIN WINDOW "
		#
		# selectMusic이 없으면 BGM이 끊기므로 두개 다 체크한다. 
		#
		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)

		## NOTE : idEditLine와 pwdEditLine은 이벤트가 서로 연결 되어있어서
		##        Event를 강제로 초기화 해주어야만 합니다 - [levites]
		self.idEditLine.SetTabEvent(0)
		self.idEditLine.SetReturnEvent(0)
		self.pwdEditLine.SetReturnEvent(0)
		self.pwdEditLine.SetTabEvent(0)

		self.connectBoard = None
		self.loginBoard = None
		self.registerBoard = None
		self.questionBoard = None
		self.idEditLine = None
		self.pwdEditLine = None
		self.inputDialog = None
		self.connectingDialog = None
		self.loadingImage = None

		self.serverBoard				= None
		self.serverList					= None
		self.channelList				= None

		# RUNUP_MATRIX_AUTH
		self.matrixQuizBoard	= None
		self.matrixAnswerInput	= None
		self.matrixAnswerOK	= None
		self.matrixAnswerCancel	= None
		# RUNUP_MATRIX_AUTH_END

		# NEWCIBN_PASSPOD_AUTH
		self.passpodBoard	= None
		self.passpodAnswerInput	= None
		self.passpodAnswerOK	= None
		self.passpodAnswerCancel = None
		# NEWCIBN_PASSPOD_AUTH_END

		self.VIRTUAL_KEY_ALPHABET_LOWERS = None
		self.VIRTUAL_KEY_ALPHABET_UPPERS = None
		self.VIRTUAL_KEY_SYMBOLS = None
		self.VIRTUAL_KEY_NUMBERS = None

		# VIRTUAL_KEYBOARD_BUG_FIX
		if self.virtualKeyboard:
			for keyIndex in xrange(0, VIRTUAL_KEYBOARD_NUM_KEYS+1):
				key = self.GetChild2("key_%d" % keyIndex)
				if key:
					key.SetEvent(None)

			self.GetChild("key_space").SetEvent(None)
			self.GetChild("key_backspace").SetEvent(None)
			self.GetChild("key_enter").SetEvent(None)
			self.GetChild("key_shift").SetToggleDownEvent(None)
			self.GetChild("key_shift").SetToggleUpEvent(None)
			self.GetChild("key_at").SetToggleDownEvent(None)
			self.GetChild("key_at").SetToggleUpEvent(None)

			self.virtualKeyboard = None

		self.KillFocus()
		self.Hide()

		self.stream.popupWindow.Close()
		self.loginFailureFuncDict=None

		ime.ClearExceptKey()

		app.HideCursor()

	def __SaveChannelInfo(self):
		try:
			file=open("channel.inf", "w")
			file.write("%d %d %d" % (self.__GetServerID(), self.__GetChannelID(), self.__GetRegionID()))
		except:
			print "LoginWindow.__SaveChannelInfo - SaveError"

	def __LoadChannelInfo(self):
		try:
			file=open("channel.inf")
			lines=file.readlines()
			
			if len(lines)>0:
				tokens=lines[0].split()

				selServerID=int(tokens[0])
				selChannelID=int(tokens[1])
				
				if len(tokens) == 3:
					regionID = int(tokens[2])

				return regionID, selServerID, selChannelID

		except:
			print "LoginWindow.__LoadChannelInfo - OpenError"
			return -1, -1, -1

	def __ExitGame(self):
		app.Exit()

	def SetIDEditLineFocus(self):
		if self.idEditLine != None:
			self.idEditLine.SetFocus()

	def SetPasswordEditLineFocus(self):
		if locale.IsEUROPE():
			if self.idEditLine != None: #0000862: [M2EU] 로그인창 팝업 에러: 종료시 먼저 None 설정됨
				self.idEditLine.SetText("")
				self.idEditLine.SetFocus() #0000685: [M2EU] 아이디/비밀번호 유추 가능 버그 수정: 무조건 아이디로 포커스가 가게 만든다

			if self.pwdEditLine != None: #0000862: [M2EU] 로그인창 팝업 에러: 종료시 먼저 None 설정됨
				self.pwdEditLine.SetText("")
		else:
			if self.pwdEditLine != None:
				self.pwdEditLine.SetFocus()								

	def OnEndCountDown(self):
		self.isNowCountDown = FALSE
		self.OnConnectFailure()

	def OnConnectFailure(self):

		if self.isNowCountDown:
			return

		snd.PlaySound("sound/ui/loginfail.wav")

		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		if app.loggined:
			self.PopupNotifyMessage(locale.LOGIN_CONNECT_FAILURE, self.__ExitGame)
		else:
			self.PopupNotifyMessage(locale.LOGIN_CONNECT_FAILURE, self.SetPasswordEditLineFocus)

	def OnHandShake(self):
		if not IsLoginDelay():
			snd.PlaySound("sound/ui/loginok.wav")
			self.PopupDisplayMessage(locale.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		if not IsLoginDelay():
			self.PopupDisplayMessage(locale.LOGIN_PROCESSING)

	def OnLoginFailure(self, error):
		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
			if PASSPOD_MSG_DICT:
				try:
					loginFailureMsg = PASSPOD_MSG_DICT[error]
				except KeyError:
					loginFailureMsg = locale.LOGIN_FAILURE_UNKNOWN + error
			else:
				loginFailureMsg = locale.LOGIN_FAILURE_UNKNOWN  + error


		#0000685: [M2EU] 아이디/비밀번호 유추 가능 버그 수정: 무조건 패스워드로 포커스가 가게 만든다
		loginFailureFunc=self.loginFailureFuncDict.get(error, self.SetPasswordEditLineFocus)

		if app.loggined:
			self.PopupNotifyMessage(loginFailureMsg, self.__ExitGame)
		else:
			self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __DisconnectAndInputID(self):
		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		self.SetIDEditLineFocus()
		net.Disconnect()

	def __DisconnectAndInputPassword(self):
		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		self.SetPasswordEditLineFocus()
		net.Disconnect()

	def __DisconnectAndInputMatrix(self):
		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		self.stream.popupWindow.Close()
		self.matrixInputChanceCount -= 1

		if self.matrixInputChanceCount <= 0:
			self.__OnCloseInputDialog()

		elif self.inputDialog:
			self.inputDialog.Show()

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = AvenueOkay.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			GetObject=self.GetChild
			self.Ausfahrbutton			= GetObject("Ausfahrbutton")
			self.WebsiteBtn				= GetObject("WebsiteBtn")
			self.serverBoard			= GetObject("ServerBoard")
			self.registerBoard			= GetObject("RegisterBoard")
			self.questionBoard			= GetObject("QuestionBoard")
			self.quesButton		    	= GetObject("QuestionButton")
			self.ques1Button		    = GetObject("Question1Button")
			self.ques2Button		    = GetObject("Question2Button")
			self.ques3Button		    = GetObject("Question3Button")
			self.ques4Button		    = GetObject("Question4Button")
			self.ques5Button		    = GetObject("Question5Button")
			self.ques6Button		    = GetObject("Question6Button")
			self.ques7Button		    = GetObject("Question7Button")
			self.ques8Button		    = GetObject("Question8Button")
			self.ques9Button		    = GetObject("Question9Button")
			self.id1EditLine			= GetObject("ID1_EditLine")
			self.pwd1EditLine			= GetObject("Password1_EditLine")
			self.pwd2EditLine			= GetObject("Password2_EditLine")
			self.mailEditLine			= GetObject("E_Mail_EditLine")
			self.delEditLine			= GetObject("Delete_EditLine")
			self.answEditLine			= GetObject("Answer_EditLine")
			self.registerButton			= GetObject("RegisterButton")
			self.registerExitButton		= GetObject("RegisterExitButton")
			self.serverList				= GetObject("ServerList")
			self.channelList			= GetObject("ChannelList")
			self.serverSelectButton		= GetObject("ServerSelectButton")			
			self.serverExitButton		= GetObject("ServerExitButton")
			self.connectBoard			= GetObject("ConnectBoard")
			self.loginBoard				= GetObject("LoginBoard")
			self.idEditLine				= GetObject("ID_EditLine")
			self.pwdEditLine			= GetObject("Password_EditLine")
			self.serverInfo				= GetObject("ConnectName")
			#self.Channel1Button	= GetObject("Channel1Button")
			self.Channel1Button	= GetObject("Channel1Button")
			self.Channel2Button	= GetObject("Channel2Button")
			self.Channel3Button	= GetObject("Channel3Button")
			self.loginButton			= GetObject("LoginButton")
			self.loginExitButton		= GetObject("LoginExitButton")
			
			## ACCMANAGER
			# RUNUP_MATRIX_AUTH
			if IsRunupMatrixAuth():
				self.matrixQuizBoard	= GetObject("RunupMatrixQuizBoard")
				self.matrixAnswerInput	= GetObject("RunupMatrixAnswerInput")
				self.matrixAnswerOK	= GetObject("RunupMatrixAnswerOK")
				self.matrixAnswerCancel	= GetObject("RunupMatrixAnswerCancel")
			# RUNUP_MATRIX_AUTH_END

			# NEWCIBN_PASSPOD_AUTH
			if IsNEWCIBNPassPodAuth():
				self.passpodBoard	= GetObject("NEWCIBN_PASSPOD_BOARD")
				self.passpodAnswerInput	= GetObject("NEWCIBN_PASSPOD_INPUT")
				self.passpodAnswerOK	= GetObject("NEWCIBN_PASSPOD_OK")
				self.passpodAnswerCancel= GetObject("NEWCIBN_PASSPOD_CANCEL")
			# NEWCIBN_PASSPOD_AUTH_END

			self.virtualKeyboard		= self.GetChild2("VirtualKeyboard")

			if self.virtualKeyboard:
				self.VIRTUAL_KEY_ALPHABET_UPPERS = Suffle(locale.VIRTUAL_KEY_ALPHABET_UPPERS)
				self.VIRTUAL_KEY_ALPHABET_LOWERS = "".join([locale.VIRTUAL_KEY_ALPHABET_LOWERS[locale.VIRTUAL_KEY_ALPHABET_UPPERS.index(e)] for e in self.VIRTUAL_KEY_ALPHABET_UPPERS])
				self.VIRTUAL_KEY_SYMBOLS = Suffle(locale.VIRTUAL_KEY_SYMBOLS)
				self.VIRTUAL_KEY_NUMBERS = Suffle(locale.VIRTUAL_KEY_NUMBERS)
				self.__VirtualKeyboard_SetAlphabetMode()
			
				self.GetChild("key_space").SetEvent(lambda : self.__VirtualKeyboard_PressKey(' '))
				self.GetChild("key_backspace").SetEvent(lambda : self.__VirtualKeyboard_PressBackspace())
				self.GetChild("key_enter").SetEvent(lambda : self.__VirtualKeyboard_PressReturn())
				self.GetChild("key_shift").SetToggleDownEvent(lambda : self.__VirtualKeyboard_SetUpperMode())
				self.GetChild("key_shift").SetToggleUpEvent(lambda : self.__VirtualKeyboard_SetLowerMode())
				self.GetChild("key_at").SetToggleDownEvent(lambda : self.__VirtualKeyboard_SetSymbolMode())
				self.GetChild("key_at").SetToggleUpEvent(lambda : self.__VirtualKeyboard_SetAlphabetMode())

		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")

		if self.IS_TEST:
			self.Channel1Button.Hide()
		else:
			self.Channel1Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickChannel1Button))

		self.serverBoard.OnKeyUp = AvenueOkay.__mem_func__(self.__ServerBoard_OnKeyUp)
		self.xServerBoard, self.yServerBoard = self.serverBoard.GetLocalPosition()

		self.serverSelectButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickSelectServerButton))
		self.serverExitButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickExitButton))

		self.loginButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickLoginButton))
		self.loginExitButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickExitButton))
		
		## ACCMANAGER
		self.Ausfahrbutton.SetEvent(AvenueOkay.__mem_func__(self.Ausfahren))
		self.WebsiteBtn.SetEvent(AvenueOkay.__mem_func__(self.__WebsiteBtn))
		self.registerButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickRegisterButton))
		self.registerExitButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickRegisterExitButton))
		
		self.quesButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestionButton))
		self.ques1Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion1Button))
		self.ques2Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion2Button))
		self.ques3Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion3Button))
		self.ques4Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion4Button))
		self.ques5Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion5Button))
		self.ques6Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion6Button))
		self.ques7Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion7Button))
		self.ques8Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion8Button))
		self.ques9Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickQuestion9Button))

		## END ACCMANAGER
		
		self.serverList.SetEvent(AvenueOkay.__mem_func__(self.__OnSelectServer))
		
		self.idEditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(AvenueOkay.__mem_func__(self.pwdEditLine.SetFocus))

		self.pwdEditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.__OnClickLoginButton))
		self.pwdEditLine.SetTabEvent(AvenueOkay.__mem_func__(self.idEditLine.SetFocus))
		self.id1EditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.pwd1EditLine.SetFocus))
		self.id1EditLine.SetTabEvent(AvenueOkay.__mem_func__(self.pwd1EditLine.SetFocus))

		self.pwd1EditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.pwd2EditLine.SetFocus))
		self.pwd1EditLine.SetTabEvent(AvenueOkay.__mem_func__(self.pwd2EditLine.SetFocus))
		
		self.pwd2EditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.mailEditLine.SetFocus))
		self.pwd2EditLine.SetTabEvent(AvenueOkay.__mem_func__(self.mailEditLine.SetFocus))

		self.mailEditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.delEditLine.SetFocus))
		self.mailEditLine.SetTabEvent(AvenueOkay.__mem_func__(self.delEditLine.SetFocus))
		
		self.delEditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.__OnClickQuestionButton))
		self.delEditLine.SetTabEvent(AvenueOkay.__mem_func__(self.__OnClickQuestionButton))
		
		self.answEditLine.SetReturnEvent(AvenueOkay.__mem_func__(self.__OnClickRegisterButton))
		self.answEditLine.SetTabEvent(AvenueOkay.__mem_func__(self.__OnClickRegisterButton))

		# RUNUP_MATRIX_AUTH
		if IsRunupMatrixAuth():			
			self.matrixAnswerOK.SAFE_SetEvent(self.__OnClickMatrixAnswerOK)
			self.matrixAnswerCancel.SAFE_SetEvent(self.__OnClickMatrixAnswerCancel)
			self.matrixAnswerInput.SAFE_SetReturnEvent(self.__OnClickMatrixAnswerOK)
		# RUNUP_MATRIX_AUTH_END

		# NEWCIBN_PASSPOD_AUTH
		if IsNEWCIBNPassPodAuth():
			self.passpodAnswerOK.SAFE_SetEvent(self.__OnClickNEWCIBNPasspodAnswerOK)
			self.passpodAnswerCancel.SAFE_SetEvent(self.__OnClickNEWCIBNPasspodAnswerCancel)
			self.passpodAnswerInput.SAFE_SetReturnEvent(self.__OnClickNEWCIBNPasspodAnswerOK)

		# NEWCIBN_PASSPOD_AUTH_END


		if IsFullBackImage():
			self.GetChild("bg1").Show()
			self.GetChild("bg2").Hide()
		return 1

	def __VirtualKeyboard_SetKeys(self, keyCodes):
		uiDefFontBackup = locale.UI_DEF_FONT
		locale.UI_DEF_FONT = locale.UI_DEF_FONT_LARGE

		keyIndex = 1
		for keyCode in keyCodes:					
			key = self.GetChild2("key_%d" % keyIndex)
			if key:
				key.SetEvent(lambda x=keyCode: self.__VirtualKeyboard_PressKey(x))
				key.SetText(keyCode)
				key.ButtonText.SetFontColor(1, 1, 1)
				keyIndex += 1
			
		for keyIndex in xrange(keyIndex, VIRTUAL_KEYBOARD_NUM_KEYS+1):
			key = self.GetChild2("key_%d" % keyIndex)
			if key:
				key.SetEvent(lambda x=' ': self.__VirtualKeyboard_PressKey(x))
				key.SetText(' ')
		
		locale.UI_DEF_FONT = uiDefFontBackup

	def __VirtualKeyboard_PressKey(self, code):
		ime.PasteString(code)
		
		#if self.virtualKeyboardMode == "ALPHABET" and self.virtualKeyboardIsUpper:
		#	self.__VirtualKeyboard_SetLowerMode()
			
	def __VirtualKeyboard_PressBackspace(self):
		ime.PasteBackspace()
		
	def __VirtualKeyboard_PressReturn(self):
		ime.PasteReturn()		

	def __VirtualKeyboard_SetUpperMode(self):
		self.virtualKeyboardIsUpper = TRUE
		
		if self.virtualKeyboardMode == "ALPHABET":
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_ALPHABET_UPPERS)
		elif self.virtualKeyboardMode == "NUMBER":
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS)
		else:
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_NUMBERS)
			
	def __VirtualKeyboard_SetLowerMode(self):
		self.virtualKeyboardIsUpper = FALSE
		
		if self.virtualKeyboardMode == "ALPHABET":
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_ALPHABET_LOWERS)
		elif self.virtualKeyboardMode == "NUMBER":
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_NUMBERS)			
		else:
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS)
			
	def __VirtualKeyboard_SetAlphabetMode(self):
		self.virtualKeyboardIsUpper = FALSE
		self.virtualKeyboardMode = "ALPHABET"		
		self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_ALPHABET_LOWERS)	

	def __VirtualKeyboard_SetNumberMode(self):			
		self.virtualKeyboardIsUpper = FALSE
		self.virtualKeyboardMode = "NUMBER"
		self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_NUMBERS)
					
	def __VirtualKeyboard_SetSymbolMode(self):		
		self.virtualKeyboardIsUpper = FALSE
		self.virtualKeyboardMode = "SYMBOL"
		self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS)
				
	def Connect(self, id, pwd):

		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()

		if IsLoginDelay():
			loginDelay = GetLoginDelay()
			self.connectingDialog = ConnectingDialog()
			self.connectingDialog.Open(loginDelay)
			self.connectingDialog.SAFE_SetTimeOverEvent(self.OnEndCountDown)
			self.connectingDialog.SAFE_SetExitEvent(self.OnPressExitKey)
			self.isNowCountDown = TRUE

		else:
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(locale.LOGIN_CONNETING, self.SetPasswordEditLineFocus, locale.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd)
		self.stream.Connect()


	def __OnClickExitButton(self):
		self.stream.SetPhaseWindow(0)

	def __SetServerInfo(self, name):
		net.SetServerInfo(name.strip())
		self.serverInfo.SetText(name)

	def __LoadLoginInfo(self, loginInfoFileName):

		try:
			loginInfo={}
			execfile(loginInfoFileName, loginInfo)
		except IOError:
			print(\
				"자동 로그인을 하시려면" + loginInfoFileName + "파일을 작성해주세요\n"\
				"\n"\
				"내용:\n"\
				"================================================================\n"\
				"addr=주소\n"\
				"port=포트\n"\
				"id=아이디\n"\
				"pwd=비밀번호\n"\
				"slot=캐릭터 선택 인덱스 (없거나 -1이면 자동 선택 안함)\n"\
				"autoLogin=자동 접속 여부\n"
				"autoSelect=자동 접속 여부\n"
				"locale=(ymir) LC_Ymir 일경우 ymir로 작동. 지정하지 않으면 korea로 작동\n"
			);

		id=loginInfo.get("id", "")
		pwd=loginInfo.get("pwd", "")

		if self.IS_TEST:
			try:
				addr=loginInfo["addr"]
				port=loginInfo["port"]
				account_addr=addr
				account_port=port

				net.SetMarkServer(addr, port)
				self.__SetServerInfo(locale.CHANNEL_TEST_SERVER_ADDR % (addr, port))
			except:
				try:
					addr=serverInfo.TESTADDR["ip"]
					port=serverInfo.TESTADDR["tcp_port"]

					net.SetMarkServer(addr, port)
					self.__SetServerInfo(locale.CHANNEL_TEST_SERVER)
				except:
					import exception
					exception.Abort("LoginWindow.__LoadLoginInfo - 테스트서버 주소가 없습니다")

		else:
			addr=loginInfo.get("addr", "")
			port=loginInfo.get("port", 0)
			account_addr=loginInfo.get("account_addr", addr)
			account_port=loginInfo.get("account_port", port)

			locale = loginInfo.get("locale", "")

			if addr and port:
				net.SetMarkServer(addr, port)

				if locale == "ymir" :
					net.SetServerInfo("천마 서버")
					self.serverInfo.SetText("Y:"+addr+":"+str(port))
				else:
					net.SetServerInfo(addr+":"+str(port))
					self.serverInfo.SetText("K:"+addr+":"+str(port))

		slot=loginInfo.get("slot", 0)
		isAutoLogin=loginInfo.get("auto", 0)
		isAutoLogin=loginInfo.get("autoLogin", 0)
		isAutoSelect=loginInfo.get("autoSelect", 0)

		self.stream.SetCharacterSlot(slot)
		self.stream.SetConnectInfo(addr, port, account_addr, account_port)
		self.stream.isAutoLogin=isAutoLogin
		self.stream.isAutoSelect=isAutoSelect

		self.id = None
		self.pwd = None		
		self.loginnedServer = None
		self.loginnedChannel = None			
		app.loggined = FALSE

		self.loginInfo = loginInfo

		if self.id and self.pwd:
			app.loggined = TRUE

		if isAutoLogin:
			self.Connect(id, pwd)
			
			print "=================================================================================="
			print "자동 로그인: %s - %s:%d %s" % (loginInfoFileName, addr, port, id)
			print "=================================================================================="

		
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func=self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, locale.UI_OK)

	# RUNUP_MATRIX_AUTH
	def BINARY_OnRunupMatrixQuiz(self, quiz):
		if not IsRunupMatrixAuth():
			return

		id		= self.GetChild("RunupMatrixID")
		id.SetText(self.idEditLine.GetText())
		
		code	= self.GetChild("RunupMatrixCode")
		
		code.SetText("".join(["[%c,%c]" % (quiz[i], quiz[i+1]) for i in xrange(0, len(quiz), 2)]))

		self.stream.popupWindow.Close()
		self.serverBoard.Hide()
		self.connectBoard.Hide()
		self.loginBoard.Hide()
		self.matrixQuizBoard.Show()
		self.matrixAnswerInput.SetFocus()

	def __OnClickMatrixAnswerOK(self):
		answer = self.matrixAnswerInput.GetText()

		print "matrix_quiz.ok"
		net.SendRunupMatrixCardPacket(answer)
		self.matrixQuizBoard.Hide()	

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open("WAITING FOR MATRIX AUTHENTICATION", 
			self.__OnClickMatrixAnswerCancel, 
			locale.UI_CANCEL)

	def __OnClickMatrixAnswerCancel(self):
		print "matrix_quiz.cancel"

		if self.matrixQuizBoard:
			self.matrixQuizBoard.Hide()	

		if self.connectBoard:
			self.connectBoard.Show()	

		if self.loginBoard:
			self.loginBoard.Show()

	# RUNUP_MATRIX_AUTH_END

	# NEWCIBN_PASSPOD_AUTH
	def BINARY_OnNEWCIBNPasspodRequest(self):
		if not IsNEWCIBNPassPodAuth():
			return

		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		self.stream.popupWindow.Close()
		self.serverBoard.Hide()
		self.connectBoard.Hide()
		self.loginBoard.Hide()
		self.passpodBoard.Show()
		self.passpodAnswerInput.SetFocus()

	def BINARY_OnNEWCIBNPasspodFailure(self):
		if not IsNEWCIBNPassPodAuth():
			return

	def __OnClickNEWCIBNPasspodAnswerOK(self):
		answer = self.passpodAnswerInput.GetText()

		print "passpod.ok"
		net.SendNEWCIBNPasspodAnswerPacket(answer)
		self.passpodAnswerInput.SetText("")
		self.passpodBoard.Hide()	

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(locale.WAIT_FOR_PASSPOD, 
			self.__OnClickNEWCIBNPasspodAnswerCancel, 
			locale.UI_CANCEL)

	def __OnClickNEWCIBNPasspodAnswerCancel(self):
		print "passpod.cancel"

		if self.passpodBoard:
			self.passpodBoard.Hide()	

		if self.connectBoard:
			self.connectBoard.Show()	

		if self.loginBoard:
			self.loginBoard.Show()

	# NEWCIBN_PASSPOD_AUTH_END


	def OnMatrixCard(self, row1, row2, row3, row4, col1, col2, col3, col4):

		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		self.matrixInputChanceCount = 3

		self.stream.popupWindow.Close()

		# CHINA_MATRIX_CARD_BUG_FIX
		## A~Z 까지 26 이내의 값이 들어있어야만 한다.
		## Python Exception Log 에서 그 이상의 값이 들어있어서 에러 방지
		## 헌데 왜 한국쪽 로그에서 이게 활용되는지는 모르겠음
		row1 = min(30, row1)
		row2 = min(30, row2)
		row3 = min(30, row3)
		row4 = min(30, row4)
		# END_OF_CHINA_MATRIX_CARD_BUG_FIX

		row1 = chr(row1 + ord('A'))
		row2 = chr(row2 + ord('A'))
		row3 = chr(row3 + ord('A'))
		row4 = chr(row4 + ord('A'))
		col1 = col1 + 1
		col2 = col2 + 1
		col3 = col3 + 1
		col4 = col4 + 1

		inputDialog = uiCommon.InputDialogWithDescription2()
		inputDialog.SetMaxLength(8)
		inputDialog.SetAcceptEvent(AvenueOkay.__mem_func__(self.__OnAcceptMatrixCardData))
		inputDialog.SetCancelEvent(AvenueOkay.__mem_func__(self.__OnCancelMatrixCardData))
		inputDialog.SetTitle(locale.INPUT_MATRIX_CARD_TITLE)
		inputDialog.SetDescription1(locale.INPUT_MATRIX_CARD_NUMBER)
		inputDialog.SetDescription2("%c%d %c%d %c%d %c%d" % (row1, col1,
															row2, col2,
															row3, col3,
															row4, col4))

		inputDialog.Open()
		self.inputDialog = inputDialog

	def __OnAcceptMatrixCardData(self):
		text = self.inputDialog.GetText()
		net.SendChinaMatrixCardPacket(text)
		if self.inputDialog:
			self.inputDialog.Hide()
		self.PopupNotifyMessage(locale.LOGIN_PROCESSING)
		return TRUE

	def __OnCancelMatrixCardData(self):
		self.SetPasswordEditLineFocus()
		self.__OnCloseInputDialog()
		self.__DisconnectAndInputPassword()
		return TRUE

	def __OnCloseInputDialog(self):
		if self.inputDialog:
			self.inputDialog.Close()
		self.inputDialog = None
		return TRUE

	def OnPressExitKey(self):
		self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def OnExit(self):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(locale.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE, app.Exit, locale.UI_OK)

	def OnUpdate(self):
		ServerStateChecker.Update()

	def EmptyFunc(self):
		pass

	#####################################################################################

	def __ServerBoard_OnKeyUp(self, key):
		if self.serverBoard.IsShow():
			if app.DIK_RETURN==key:
				self.__OnClickSelectServerButton()
		return TRUE

	def __GetRegionID(self):
		return 0

	def __GetServerID(self):
		return self.serverList.GetSelectedItem()

	def __GetChannelID(self):
		return self.channelList.GetSelectedItem()

	# SEVER_LIST_BUG_FIX
	def __ServerIDToServerIndex(self, regionID, targetServerID):
		try:
			regionDict = serverInfo.REGION_DICT[regionID]
		except KeyError:
			return -1

		retServerIndex = 0
		for eachServerID, regionDataDict in regionDict.items():
			if eachServerID == targetServerID:
				return retServerIndex

			retServerIndex += 1		
		
		return -1

	def __ChannelIDToChannelIndex(self, channelID):
		return channelID - 1
	# END_OF_SEVER_LIST_BUG_FIX

	def __OpenServerBoard(self):
		constInfo.ChannelID = 1
		self.stream.SetConnectInfo(s_info.SERVERIP, s_info.GiveMePort(1), s_info.SERVERIP, s_info.GiveMePort("auth"))
		net.SetServerInfo(s_info.SERVERNAME + " - CH 1")
		net.SetMarkServer(s_info.SERVERIP, s_info.GiveMePort(1))
		self.serverInfo.SetText(s_info.SERVERNAME + " - CH 1")
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")
		self.Channel1Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickChannel1Button))
		self.Channel2Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickChannel2Button))
		self.Channel3Button.SetEvent(AvenueOkay.__mem_func__(self.__OnClickChannel3Button))
			
		self.serverExitButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickExitServerButton))
		self.serverExitButton.SetText(locale.UI_CLOSE)

		# RUNUP_MATRIX_AUTH
		if IsRunupMatrixAuth():
			self.matrixQuizBoard.Hide()
		# RUNUP_MATRIX_AUTH_END

		# NEWCIBN_PASSPOD_AUTH
		if IsNEWCIBNPassPodAuth():
			self.passpodBoard.Hide()
		# NEWCIBN_PASSPOD_AUTH_END

		self.serverBoard.SetPosition(self.xServerBoard, wndMgr.GetScreenHeight())
		self.serverBoard.Hide()

		if self.virtualKeyboard:
			self.virtualKeyboard.Hide()
	
		if app.loggined:
			self.Connect(self.id, self.pwd)
			self.connectBoard.Hide()
			self.loginBoard.Hide()
		elif not self.stream.isAutoLogin:
			self.connectBoard.Show()
			self.loginBoard.Show()

		## if users have the login infomation, then don't initialize.2005.9 haho
		if self.idEditLine == None:
			self.idEditLine.SetText("")
		if self.pwdEditLine == None:
			self.pwdEditLine.SetText("")

		self.idEditLine.SetFocus()

		global SKIP_LOGIN_PHASE
		if SKIP_LOGIN_PHASE:
			if not self.loginInfo:
				self.connectBoard.Hide()

	def __OpenLoginBoard(self):
		self.BGBoard.Hide()
		print "XMAS_SNOW ON"
		background.EnableSnow(1)
			
		self.serverExitButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickExitServerButton))
		self.serverExitButton.SetText(locale.UI_CLOSE)

		# RUNUP_MATRIX_AUTH
		if IsRunupMatrixAuth():
			self.matrixQuizBoard.Hide()
		# RUNUP_MATRIX_AUTH_END

		# NEWCIBN_PASSPOD_AUTH
		if IsNEWCIBNPassPodAuth():
			self.passpodBoard.Hide()
		# NEWCIBN_PASSPOD_AUTH_END

		self.serverBoard.SetPosition(self.xServerBoard, wndMgr.GetScreenHeight())
		self.serverBoard.Hide()

		if self.virtualKeyboard:
			self.virtualKeyboard.Show()

		if app.loggined:
			self.Connect(self.id, self.pwd)
			self.connectBoard.Hide()
			self.loginBoard.Hide()
		elif not self.stream.isAutoLogin:
			self.connectBoard.Show()
			self.loginBoard.Show()

		## if users have the login infomation, then don't initialize.2005.9 haho
		if self.idEditLine == None:
			self.idEditLine.SetText("")
		if self.pwdEditLine == None:
			self.pwdEditLine.SetText("")

		self.idEditLine.SetFocus()

		global SKIP_LOGIN_PHASE
		if SKIP_LOGIN_PHASE:
			if not self.loginInfo:
				self.connectBoard.Hide()

	def __OnSelectRegionGroup(self):
		self.__RefreshServerList()

	def __OnSelectSettlementArea(self):
		# SEVER_LIST_BUG_FIX
		regionID = self.__GetRegionID()
		serverID = self.serverListOnRegionBoard.GetSelectedItem()

		serverIndex = self.__ServerIDToServerIndex(regionID, serverID)
		self.serverList.SelectItem(serverIndex)
		# END_OF_SEVER_LIST_BUG_FIX
		
		self.__OnSelectServer()

	def __RefreshServerList(self):
		regionID = self.__GetRegionID()
		
		if not serverInfo.REGION_DICT.has_key(regionID):
			return

		self.serverList.ClearItem()

		regionDict = serverInfo.REGION_DICT[regionID]

		# SEVER_LIST_BUG_FIX
		visible_index = 1
		for id, regionDataDict in regionDict.items():
			name = regionDataDict.get("name", "noname")
			if locale.IsBRAZIL() or locale.IsCANADA():
				self.serverList.InsertItem(id, "%s" % (name))
			else:
				if locale.IsCIBN10():			
					if name[0] == "#":
						self.serverList.InsertItem(-1, "  %s" % (name[1:]))
					else:
						self.serverList.InsertItem(id, "  %s" % (name))
						visible_index += 1
				else:
					self.serverList.InsertItem(id, "  %02d. %s" % (visible_index, name))
					
					visible_index += 1
		
		# END_OF_SEVER_LIST_BUG_FIX

	def __OnSelectServer(self):
		self.__OnCloseInputDialog()
		self.__RequestServerStateList()
		self.__RefreshServerStateList()

	def __RequestServerStateList(self):
		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()

		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except:
			print " __RequestServerStateList - serverInfo.REGION_DICT(%d, %d)" % (regionID, serverID)
			return

		for id, channelDataDict in channelDict.items():
			key=channelDataDict["key"]
			ip=channelDataDict["ip"]
			udp_port=channelDataDict["udp_port"]
			ServerStateChecker.Request(key, ip, udp_port)

	def __RefreshServerStateList(self):

		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()
		bakChannelID = self.channelList.GetSelectedItem()

		self.channelList.ClearItem()

		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except:
			print " __RequestServerStateList - serverInfo.REGION_DICT(%d, %d)" % (regionID, serverID)
			return

		for channelID, channelDataDict in channelDict.items():
			channelName = channelDataDict["name"]
			channelState = channelDataDict["state"]
			self.channelList.InsertItem(channelID, " %s %s" % (channelName, channelState))

		self.channelList.SelectItem(bakChannelID-1)

	def __GetChannelName(self, regionID, selServerID, selChannelID):
		try:
			return serverInfo.REGION_DICT[regionID][selServerID]["channel"][selChannelID]["name"]
		except KeyError:
			if 9==selChannelID:
				return locale.CHANNEL_PVP
			else:
				return locale.CHANNEL_NORMAL % (selChannelID)

	def NotifyChannelState(self, addrKey, state):
		try:
			stateName=serverInfo.STATE_DICT[state]
		except:
			stateName=serverInfo.STATE_NONE

		regionID=int(addrKey/1000)
		serverID=int(addrKey/10) % 100
		channelID=addrKey%10

		try:
			serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["state"] = stateName
			self.__RefreshServerStateList()

		except:
			import exception
			exception.Abort(locale.CHANNEL_NOT_FIND_INFO)

	def __OnClickExitServerButton(self):
		print "exit server"
		self.__OpenLoginBoard()			

		if IsFullBackImage():
			self.GetChild("bg1").Hide()
			self.GetChild("bg2").Show()
			

	def __OnClickSelectRegionButton(self):
		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()

		if (not serverInfo.REGION_DICT.has_key(regionID)):
			self.PopupNotifyMessage(locale.CHANNEL_SELECT_REGION)
			return

		if (not serverInfo.REGION_DICT[regionID].has_key(serverID)):
			self.PopupNotifyMessage(locale.CHANNEL_SELECT_SERVER)
			return		

		self.__SaveChannelInfo()

		self.serverExitButton.SetEvent(AvenueOkay.__mem_func__(self.__OnClickExitServerButton))
		self.serverExitButton.SetText(locale.UI_CLOSE)

		self.__RefreshServerList()
		self.__OpenServerBoard()

	def __OnClickSelectServerButton(self):
		if IsFullBackImage():
			self.GetChild("bg1").Show()
			self.GetChild("bg2").Hide()

		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()
		channelID = self.__GetChannelID()

		if (not serverInfo.REGION_DICT.has_key(regionID)):
			self.PopupNotifyMessage(locale.CHANNEL_SELECT_REGION)
			return

		if (not serverInfo.REGION_DICT[regionID].has_key(serverID)):
			self.PopupNotifyMessage(locale.CHANNEL_SELECT_SERVER)
			return

		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except KeyError:
			return

		try:
			state = channelDict[channelID]["state"]
		except KeyError:
			self.PopupNotifyMessage(locale.CHANNEL_SELECT_CHANNEL)
			return

		# 상태가 FULL 과 같으면 진입 금지
		if state == serverInfo.STATE_DICT[3]: 
			self.PopupNotifyMessage(locale.CHANNEL_NOTIFY_FULL)
			return

		self.__SaveChannelInfo()

		try:
			serverName = serverInfo.REGION_DICT[regionID][serverID]["name"]
			channelName = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["name"]
			addrKey = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["key"]
		except:
			print " ERROR __OnClickSelectServerButton(%d, %d, %d)" % (regionID, serverID, channelID)
			serverName = locale.CHANNEL_EMPTY_SERVER
			channelName = locale.CHANNEL_NORMAL % channelID

		self.__SetServerInfo("%s, %s " % (s_info.SERVERNAME, channelName))

		try:
			ip = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["ip"]
			tcp_port = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["tcp_port"]
		except:
			import exception
			exception.Abort("LoginWindow.__OnClickSelectServerButton - 서버 선택 실패")

		try:
			account_ip = serverInfo.REGION_AUTH_SERVER_DICT[regionID][serverID]["ip"]
			account_port = serverInfo.REGION_AUTH_SERVER_DICT[regionID][serverID]["port"]
		except:
			account_ip = 0
			account_port = 0

		try:
			markKey = regionID*1000 + serverID*10
			markAddrValue=serverInfo.MARKADDR_DICT[markKey]
			net.SetMarkServer(markAddrValue["ip"], markAddrValue["tcp_port"])
			app.SetGuildMarkPath(markAddrValue["mark"])
			# GUILD_SYMBOL
			app.SetGuildSymbolPath(markAddrValue["symbol_path"])
			# END_OF_GUILD_SYMBOL

		except:
			import exception
			exception.Abort("LoginWindow.__OnClickSelectServerButton - 마크 정보 없음")

		self.stream.SetConnectInfo(ip, tcp_port, account_ip, account_port)

		self.__OpenLoginBoard() 
		
	def __OnClickChannel1Button(self):
		self.stream.SetConnectInfo(s_info.SERVERIP, s_info.GiveMePort(1),s_info.SERVERIP, s_info.GiveMePort("auth"))
		net.SetServerInfo(s_info.SERVERNAME + " - CH 1")
		net.SetMarkServer(s_info.SERVERIP, s_info.GiveMePort(1))
		self.serverInfo.SetText(s_info.SERVERNAME + " - CH 1")
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")  
	def __OnClickChannel2Button(self):
		self.stream.SetConnectInfo(s_info.SERVERIP, s_info.CH2PORT,s_info.SERVERIP, s_info.GiveMePort("auth"))
		net.SetServerInfo(s_info.SERVERNAME + " - CH 2")
		net.SetMarkServer(s_info.SERVERIP, s_info.CH2PORT)
		self.serverInfo.SetText(s_info.SERVERNAME + " - CH 2")
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10") 
	def __OnClickChannel3Button(self):
		self.stream.SetConnectInfo(s_info.SERVERIP, s_info.CH3PORT,s_info.SERVERIP, s_info.GiveMePort("auth"))
		net.SetServerInfo(s_info.SERVERNAME + " - CH 3")
		net.SetMarkServer(s_info.SERVERIP, s_info.CH3PORT)
		self.serverInfo.SetText(s_info.SERVERNAME + " - CH 3")
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10") 

	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()		

		if len(id)==0:
			self.PopupNotifyMessage(locale.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(locale.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return

		self.Connect(id, pwd)

	def __OnClickQuestionButton(self):
		self.registerBoard.Hide()
		self.serverBoard.Hide()
		self.connectBoard.Hide()
		self.loginBoard.Hide()
		self.virtualKeyboard.Hide()
		self.questionBoard.Show()
		
	def __OnClickQuestion1Button(self):
		constInfo.QUESTION = 1
		self.registerBoard.Show()
		self.questionBoard.Hide()

	def __OnClickQuestion2Button(self):
		constInfo.QUESTION = 2
		self.registerBoard.Show()
		self.questionBoard.Hide()
		
	def __OnClickQuestion3Button(self):
		constInfo.QUESTION = 3
		self.registerBoard.Show()
		self.questionBoard.Hide()
		
	def __OnClickQuestion4Button(self):
		constInfo.QUESTION = 4
		self.registerBoard.Show()
		self.questionBoard.Hide()
		
	def __OnClickQuestion5Button(self):
		constInfo.QUESTION = 5
		self.registerBoard.Show()
		self.questionBoard.Hide()
		
	def __OnClickQuestion6Button(self):
		constInfo.QUESTION = 6
		self.registerBoard.Show()
		self.questionBoard.Hide()

	def __OnClickQuestion7Button(self):
		constInfo.QUESTION = 7
		self.registerBoard.Show()
		self.questionBoard.Hide()
		
	def __OnClickQuestion8Button(self):
		constInfo.QUESTION = 8
		self.registerBoard.Show()
		self.questionBoard.Hide()
		
	def __OnClickQuestion9Button(self):
		constInfo.QUESTION = 9
		self.registerBoard.Show()
		self.questionBoard.Hide()
		
	def __OnClickRegisterExitButton(self):
		self.connectBoard.Show()
		self.loginBoard.Show()
		self.virtualKeyboard.Show()
		
		self.registerBoard.Hide()
		self.serverBoard.Hide()
		self.idEditLine.SetText(self.id1EditLine.GetText())
		self.pwdEditLine.SetText(self.pwd1EditLine.GetText())
		
	def __OnClickRegisterButton(self):
		self.Close()

	def slide(self,delay):
		count = 1
		y=-117
		global arbeitet
		arbeitet=1
		while count < 39:
			time.sleep(delay)
			count += 1
			y=y+3
			self.connectBoard.SetPosition( (wndMgr.GetScreenWidth() - 564) / 2,y)
		arbeitet=0		

	def slideback(self,delay):
		count = 1
		y=0
		global arbeitet
		arbeitet=1
		while count < 39:
			time.sleep(delay)
			count += 1
			y=y-3
			self.connectBoard.SetPosition( (wndMgr.GetScreenWidth()-564) / 2, y)
		arbeitet=0

	def Ausfahren(self):
		channels = [1, 2, 3]
		global AKTCHANNEL
		if AKTCHANNEL+1 >= 3:
			AKTCHANNEL = 0
			self.stream.SetConnectInfo(s_info.SERVERIP, s_info.GiveMePort(1), s_info.SERVERIP, s_info.GiveMePort("auth"))
			net.SetServerInfo(s_info.SERVERNAME + " - CH 1")
			net.SetMarkServer(s_info.SERVERIP, s_info.GiveMePort(1))
			self.serverInfo.SetText(s_info.SERVERNAME + " - CH 1")
			app.SetGuildMarkPath("10.tga")
			app.SetGuildSymbolPath("10")
		else:
			AKTCHANNEL += 1
			self.stream.SetConnectInfo(s_info.SERVERIP, s_info.GiveMePort(AKTCHANNEL), s_info.SERVERIP, s_info.GiveMePort("auth"))
			net.SetServerInfo(s_info.SERVERNAME + " - CH "+str(channels[AKTCHANNEL]))
			net.SetMarkServer(s_info.SERVERIP, s_info.GiveMePort(AKTCHANNEL))
			self.serverInfo.SetText(s_info.SERVERNAME + " - CH "+str(channels[AKTCHANNEL]))
			app.SetGuildMarkPath("10.tga")
			app.SetGuildSymbolPath("10")

	def __WebsiteBtn(self):
		os.startfile("http://google.de")
