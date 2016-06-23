import os
os.system('nmcli nm wifi off')
os.system('echo 6088 | sudo -S macchanger -a wlan0')
os.system('nmcli nm wifi on')
