#Run this on master computer
#Install vnstat on each server "sudo apt-get install vnstat"
#Enable vnstat by using "sudo vnstat --enable"
import os
import sys
path = os.path.dirname(os.path.realpath(sys.argv[0]))
path = path+'/data_monitor/'
os.system('sudo pip install paramiko')
os.system('sudo pip install xlwt')
os.system('wget https://raw.githubusercontent.com/bedapudi6788/Python-scripts/master/data_monitor/data_monitor.tar.gz')
os.system('tar -xzf data_monitor.tar.gz')
os.system('(crontab -l 2>/dev/null; echo "@reboot nohup python '+path+'data_monitor.py &") | crontab -')

print 'Run server_add.py to add servers and their passwords'
print 'PLEASE DO NOT MANUALLY ADD ANYTHING TO servers.txt FILE'
print 'IF YOU WANT TO ADD A SEVER RUN server_add.py'
print 'Install vnstat and enable vnstat on each server'