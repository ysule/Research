import os
import sys
path = os.path.dirname(os.path.realpath(sys.argv[0]))
os.system('wget https://raw.githubusercontent.com/bedapudi6788/Python-scripts/master/macchanger.py')
os.system('(crontab -l 2>/dev/null; echo "@reboot nohup python '+path+'macchanger.py &") | crontab -')
