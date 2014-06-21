SERVERIP = 'IP-ADRESSE'
SERVERNAME = 'SERVERNAME'

def GiveMePort(channel):
	if channel == 'auth':
		return 11002	## Loginport
	else:
		ports = [
			13070,		## Ch1 Port
			14070,		## Ch2 Port
			15070]		## Ch3 Port
		return ports[channel - 1]
