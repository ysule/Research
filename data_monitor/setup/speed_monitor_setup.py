#Run this on each server computer
#Install iptraf on each server "sudo apt-get install iptraf"
import os
import sys
path = os.path.dirname(os.path.realpath(sys.argv[0]))
path = path+'/speed_monitor/'
os.system('sudo pip install paramiko')
os.system('sudo pip install netifaces')
os.system('wget https://raw.githubusercontent.com/bedapudi6788/Python-scripts/master/data_monitor/speed_monitor.tar.gz')
os.system('tar -xzf speed_monitor.tar.gz')
os.system('(crontab -l 2>/dev/null; echo "@reboot nohup python '+path+'speed_monitor_v1.2.py &") | crontab -')

print 'Run server_add.py to add servers and their passwords'
print 'PLEASE DO NOT MANUALLY ADD ANYTHING TO servers.txt FILE'
print 'IF YOU WANT TO ADD A SEVER RUN server_add.py'
print 'Install vnstat and enable vnstat on each server'