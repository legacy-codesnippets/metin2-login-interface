import uiScriptLocale
		
LOCALE_PATH = uiScriptLocale.LOGIN_PATH
SERVER_BOARD_HEIGHT = 220
SERVER_LIST_HEIGHT = 170

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "bg1", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/de/ui/login.sub",
		},
		{
			"name" : "bg2", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/de/ui/login.sub",
		},
		{
			"name" : "logo1", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/de/ui/logo.sub",
		},
		## VirtualKeyboard
		{
			'name' : 'VirtualKeyboard',
			'type' : 'thinboard',
			'x' : (SCREEN_WIDTH - 564) / 2,
			'y' : SCREEN_HEIGHT - 310,
			'width' : 564,
			'height' : 254,
			'children' : 
			(
				{
					'name' : 'key_at',
					'type' : 'toggle_button',
					'x' : 40,
					'y' : 186,
					'default_image' : 'locale/de/ui/vkey/key_at.tga',
					'down_image' : 'locale/de/ui/vkey/key_at_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_at_over.tga',
				},
				{
					'name' : 'key_backspace',
					'type' : 'button',
					'x' : 498,
					'y' : 186,
					'default_image' : 'locale/de/ui/vkey/key_backspace.tga',
					'down_image' : 'locale/de/ui/vkey/key_backspace_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_backspace_over.tga',
				},
				{
					'name' : 'key_enter',
					'type' : 'button',
					'x' : 439,
					'y' : 186,
					'default_image' : 'locale/de/ui/vkey/key_enter.tga',
					'down_image' : 'locale/de/ui/vkey/key_enter_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_enter_over.tga',
				},
				{
					'name' : 'key_shift',
					'type' : 'toggle_button',
					'x' : 86,
					'y' : 186,
					'default_image' : 'locale/de/ui/vkey/key_shift.tga',
					'down_image' : 'locale/de/ui/vkey/key_shift_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_shift_over.tga',
				},
				{
					'name' : 'key_space',
					'type' : 'button',
					'x' : 145,
					'y' : 186,
					'default_image' : 'locale/de/ui/vkey/key_space.tga',
					'down_image' : 'locale/de/ui/vkey/key_space_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_space_over.tga',
				},
				{
					'name' : 'key_1',
					'type' : 'button',
					'x' : 40,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_2',
					'type' : 'button',
					'x' : 80,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_3',
					'type' : 'button',
					'x' : 120,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_4',
					'type' : 'button',
					'x' : 160,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_5',
					'type' : 'button',
					'x' : 200,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_6',
					'type' : 'button',
					'x' : 240,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_7',
					'type' : 'button',
					'x' : 280,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_8',
					'type' : 'button',
					'x' : 320,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_9',
					'type' : 'button',
					'x' : 360,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_10',
					'type' : 'button',
					'x' : 400,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_11',
					'type' : 'button',
					'x' : 440,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_12',
					'type' : 'button',
					'x' : 480,
					'y' : 24,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_13',
					'type' : 'button',
					'x' : 40,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_14',
					'type' : 'button',
					'x' : 80,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_15',
					'type' : 'button',
					'x' : 120,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_16',
					'type' : 'button',
					'x' : 160,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_17',
					'type' : 'button',
					'x' : 200,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_18',
					'type' : 'button',
					'x' : 240,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_19',
					'type' : 'button',
					'x' : 280,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_20',
					'type' : 'button',
					'x' : 320,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_21',
					'type' : 'button',
					'x' : 360,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_22',
					'type' : 'button',
					'x' : 400,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_23',
					'type' : 'button',
					'x' : 440,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_24',
					'type' : 'button',
					'x' : 480,
					'y' : 63,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_25',
					'type' : 'button',
					'x' : 60,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_26',
					'type' : 'button',
					'x' : 100,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_27',
					'type' : 'button',
					'x' : 140,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_28',
					'type' : 'button',
					'x' : 180,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_29',
					'type' : 'button',
					'x' : 220,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_30',
					'type' : 'button',
					'x' : 260,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_31',
					'type' : 'button',
					'x' : 300,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_32',
					'type' : 'button',
					'x' : 340,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_33',
					'type' : 'button',
					'x' : 380,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_34',
					'type' : 'button',
					'x' : 420,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_35',
					'type' : 'button',
					'x' : 460,
					'y' : 104,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_36',
					'type' : 'button',
					'x' : 60,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_37',
					'type' : 'button',
					'x' : 100,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_38',
					'type' : 'button',
					'x' : 140,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_39',
					'type' : 'button',
					'x' : 180,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_40',
					'type' : 'button',
					'x' : 220,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_41',
					'type' : 'button',
					'x' : 260,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_42',
					'type' : 'button',
					'x' : 300,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_43',
					'type' : 'button',
					'x' : 340,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_44',
					'type' : 'button',
					'x' : 380,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_45',
					'type' : 'button',
					'x' : 420,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_46',
					'type' : 'button',
					'x' : 460,
					'y' : 144,
					'default_image' : 'locale/de/ui/vkey/key_normal.tga',
					'down_image' : 'locale/de/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/de/ui/vkey/key_normal_over.tga',
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x" : 470,
					"y" : 229,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : "Beenden",
				},
			)
		},
		## QuestionBoard
		{
			"name" : "QuestionBoard",
			"type" : "board",

			"x" : (SCREEN_WIDTH - 288) / 2 + 36,
			"y" : SCREEN_HEIGHT - 260 - 180,
			"width" : 208,
			"height" : 310,

			"children" :
			(
				{
					"name" : "Question1Button",
					"type" : "button",

					"x" : 15,
					"y" : - 120,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Wie ist der Name deines Haustieres?",
				},
				{
					"name" : "Question2Button",
					"type" : "button",

					"x" : 15,
					"y" : - 90,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Was ist dein Lieblings-Buch?",
				},
				{
					"name" : "Question3Button",
					"type" : "button",

					"x" : 15,
					"y" : - 60,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Was ist dein Lieblings-Film?",
				},
				{
					"name" : "Question4Button",
					"type" : "button",

					"x" : 15,
					"y" : - 30,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Wie lautet deine Lieblings-Farbe?",
				},
				{
					"name" : "Question5Button",
					"type" : "button",

					"x" : 15,
					"y" : 0,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Wie heißt deien Mutter?",
				},
				{
					"name" : "Question6Button",
					"type" : "button",

					"x" : 15,
					"y" : 30,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Wie heißt dein Vater?",
				},
				{
					"name" : "Question7Button",
					"type" : "button",

					"x" : 15,
					"y" : 60,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Wie heißt dein Bruder?",
				},
				{
					"name" : "Question8Button",
					"type" : "button",

					"x" : 15,
					"y" : 90,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Wie heißt deine Schwester?",
				},
				{
					"name" : "Question9Button",
					"type" : "button",

					"x" : 15,
					"y" : 120,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",

					"text" : "Was ist deine Lieblings-Sportart?",
				},
			),
		},
		## RegisterBoard
		{
			"name" : "RegisterBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - 288) / 2,
			"y" : SCREEN_HEIGHT - 260 - 180,
			"width" : 288,
			"height" : 260,

			"children" :
			(	
				{
					"name" : "id_slot",
					"type" : "image",

					"x" : 130,
					"y" : 16,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
				},
				{
					"name" : "ID",
					"type" : "text",

					"x" : 30,
					"y" : - 107,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : "Account ID:",
				},
				{
					"name" : "ID1_EditLine",
					"type" : "editline",

					"x" : 135,
					"y" : 18,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				
				{
					"name" : "pwd_slot",
					"type" : "image",

					"x" : 130,
					"y" : 43,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
				},
				{
					"name" : "PWD",
					"type" : "text",

					"x" : 30,
					"y" : - 80,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : "Passwort:",
				},
				{
					"name" : "Password1_EditLine",
					"type" : "editline",

					"x" : 135,
					"y" : 45,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"secret_flag" : 1,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "pwd2_slot",
					"type" : "image",

					"x" : 130,
					"y" : 70,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
				},
				{
					"name" : "PWD2",
					"type" : "text",

					"x" : 30,
					"y" : - 53,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : "Passwort:",
				},
				{
					"name" : "Password2_EditLine",
					"type" : "editline",

					"x" : 135,
					"y" : 72,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"secret_flag" : 1,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "e_mail_slot",
					"type" : "image",

					"x" : 130,
					"y" : 97,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
				},
				{
					"name" : "MAIL",
					"type" : "text",

					"x" : 30,
					"y" : - 26,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : "E-Mail:",
				},
				{
					"name" : "E_Mail_EditLine",
					"type" : "editline",

					"x" : 135,
					"y" : 99,

					"width" : 120,
					"height" : 18,

					"input_limit" : 30,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "delete_slot",
					"type" : "image",

					"x" : 130,
					"y" : 124,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
				},
				{
					"name" : "Delete",
					"type" : "text",

					"x" : 30,
					"y" : 1,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : "Löschcode:",
				},
				{
					"name" : "Delete_EditLine",
					"type" : "editline",

					"x" : 135,
					"y" : 126,

					"width" : 120,
					"height" : 18,

					"input_limit" : 7,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "Ques",
					"type" : "text",

					"x" : 30,
					"y" : 28,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : "Sicherheitsfrage:",
				},
				{
					"name" : "QuestionButton",
					"type" : "button",

					"x" : 150,
					"y" : 150,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : "Sicherheitsfrage",
				},
				{
					"name" : "Answ_slot",
					"type" : "image",

					"x" : 130,
					"y" : 178,

					"image" : "d:/ymir work/ui/public/Parameter_Slot_05.sub",
				},
				{
					"name" : "Answ",
					"type" : "text",

					"x" : 30,
					"y" : 55,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : "Antwort:",
				},
				{
					"name" : "Answer_EditLine",
					"type" : "editline",

					"x" : 135,
					"y" : 180,

					"width" : 120,
					"height" : 18,

					"input_limit" : 20,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "RegisterButton",
					"type" : "button",

					"x" : 45,
					"y" : 220,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : "Registrieren",
				},
				{
					"name" : "RegisterExitButton",

					"type" : "button",

					"x" : 155,
					"y" : 220,



					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : "Zurück",
				},
			),

		},
		## ConnectBoard
		{
			"name" : "ConnectBoard",
			"type" : "expanded_image",
			"image" : "locale/de/ui/login/channel.tga",

			"x" : (SCREEN_WIDTH - 564) / 2,
			"y" : -117,
			"width" : 564,
			"height" : 117,

			"children" :
			(
				{
					"name" : "Channel1Button",
					"type" : "button",

					"x" : 0,
					"y" : 0,
					"vertical_align" : "center",
					"horizontal_align" : "left",

					"default_image" : "locale/de/ui/login/login_btn1.tga",
					"over_image" : "locale/de/ui/login/login_btn2.tga",
					"down_image" : "locale/de/ui/login/login_btn1.tga",

					"text" : "CH 1",
				},
				{
					"name" : "Channel2Button",
					"type" : "button",

					"x" : 119,
					"y" : 0,
					"vertical_align" : "center",
					"horizontal_align" : "right",

					"default_image" : "locale/de/ui/login/login_btn1.tga",
					"over_image" : "locale/de/ui/login/login_btn2.tga",
					"down_image" : "locale/de/ui/login/login_btn1.tga",

					"text" : "CH 2",
				},
				{
					"name" : "Channel3Button",
					"type" : "button",

					"x" : 0,
					"y" : 0,
					"vertical_align" : "top",
					"horizontal_align" : "center",

					"default_image" : "locale/de/ui/login/login_btn1.tga",
					"over_image" : "locale/de/ui/login/login_btn2.tga",
					"down_image" : "locale/de/ui/login/login_btn1.tga",

					"text" : "CH 3",
				},
			),
		},

		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : (SCREEN_WIDTH/2) - 228,
			"y" : 35,

			"image" : LOCALE_PATH + "loginwindow.sub",

			"children" :
			(
				{
					"name" : "ConnectName",
					"type" : "text",

					"x" : 0,
					"y" : 24.5,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.LOGIN_DEFAULT_SERVERADDR,
				},
				{
					"name" : "ID_EditLine",
					"type" : "editline",

					"x" : 100,
					"y" : 100,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "Password_EditLine",
					"type" : "editline",

					"x" : 100,
					"y" : 148,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"secret_flag" : 1,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"horizontal_align" : "center",
					"x" : 0,
					"y" : 215,

					"width" : 272,
					"height" : 44,

					"default_image" : "locale/de/ui/login/connect.tga",
					"over_image" : "locale/de/ui/login/connect_h.tga",
					"down_image" : "locale/de/ui/login/connect_a.tga",
				},
			),
		},

		## ServerBoard
		{
			"name" : "ServerBoard",
			"type" : "thinboard",

			"x" : 0,
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT - 150,
			"width" : 375,
			"height" : SERVER_BOARD_HEIGHT,
			"horizontal_align" : "center",

			"children" :
			(

				## Title
				{
					"name" : "Title",
					"type" : "text",

					"x" : 0,
					"y" : 12,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text" : uiScriptLocale.LOGIN_SELECT_TITLE,
				},

				## Horizontal
				{
					"name" : "HorizontalLine1",
					"type" : "line",

					"x" : 10,
					"y" : 34,
					"width" : 354,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "HorizontalLine2",
					"type" : "line",

					"x" : 10,
					"y" : 35,
					"width" : 355,
					"height" : 0,
					"color" : 0xff111111,
				},

				## Vertical
				{
					"name" : "VerticalLine1",
					"type" : "line",

					"x" : 246,
					"y" : 38,
					"width" : 0,
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff777777,
				},
				{
					"name" : "VerticalLine2",
					"type" : "line",

					"x" : 247,
					"y" : 38,
					"width" : 0,
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff111111,
				},

				## ListBox
				{
					"name" : "ServerList",
					"type" : "listbox2",

					"x" : 10,
					"y" : 40,
					"width" : 232,
					"height" : SERVER_LIST_HEIGHT,
					"row_count" : 18,
					"item_align" : 0,
				},
				{
					"name" : "ChannelList",
					"type" : "listbox",

					"x" : 255,
					"y" : 40,
					"width" : 109,
					"height" : SERVER_LIST_HEIGHT,

					"item_align" : 0,
				},

				## Buttons
			),
		},
		# Menu
		{
			"name" : "MenuBoard",
			"type" : "expanded_image",
			
			"image" : "locale/de/ui/login/menubar.tga",

			"x" : 0,
			"y" : SCREEN_HEIGHT - 68,
			"width" : 9100,
			"height" : 68,

			"children" :
			(
				{
					"name" : "ServerSelectButton",
					"type" : "button",

					"x" : 267,
					"y" : SERVER_LIST_HEIGHT,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.OK,
				},
				{
					"name" : "ServerExitButton",
					"type" : "button",

					"x" : 267,
					"y" : SERVER_LIST_HEIGHT + 22,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_EXIT,
				},
				{
					"name" : "Ausfahrbutton",
					"type" : "button",

					"vertical_align" : "center",
					"x" : 20,
					"y" : 0,

					"default_image" : "locale/de/ui/login/channel.tga",
					"over_image" : "locale/de/ui/login/channel_h.tga",
					"down_image" : "locale/de/ui/login/channel_a.tga",
				},
				{
					"name" : "WebsiteBtn",
					"type" : "button",

					"vertical_align" : "center",
					"x" : 140,
					"y" : 0,

					"default_image" : "locale/de/ui/login/website.tga",
					"over_image" : "locale/de/ui/login/website_h.tga",
					"down_image" : "locale/de/ui/login/website_a.tga",
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"vertical_align" : "center",
					"x" : SCREEN_WIDTH - 150,
					"y" : 0,

					"default_image" : "locale/de/ui/login/exit.tga",
					"over_image" : "locale/de/ui/login/exit_h.tga",
					"down_image" : "locale/de/ui/login/exit_a.tga",
				},
			),
		},
	),
}