import os

try:
	os.system('netsh interface set interface name="Wi-Fi 4" admin=ENABLED')
except:
	print("there was an error.")