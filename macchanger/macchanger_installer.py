import os
import sys
path = os.path.dirname(os.path.realpath(sys.argv[0]))
password = raw_input("Enter your sudo password:")
code = "import os\nos.system('nmcli nm wifi off')\nos.system('echo "+password+" | sudo -S macchanger -a wlan0')\nos.system('nmcli nm wifi on')"
os.system('rm macchanger.py')
os.system('touch macchanger.py')
f = open('macchanger.py','w')
f.write(code)
f.flush()
os.system('(crontab -l 2>/dev/null; echo "@reboot nohup python '+path+'macchanger.py &") | crontab -')
x = raw_input("Do you want your macaddress to be changed now? (y/n)")
if x == 'y':
    os.system('python macchanger.py')
