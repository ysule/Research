#Run this on each server computer
#Install iptraf on each server "sudo apt-get install iptraf"
import os

os.system('sudo pip install netifaces')
os.system('wget https://raw.githubusercontent.com/bedapudi6788/Python-scripts/master/data_monitor/data_monitor.tar.gz')
os.system('tar -xzf data_monitor.tar.gz')
os.system('(crontab -l 2>/dev/null; echo "@reboot nohup python '+path+'data_monitor.py &") | crontab -')

print 'Run server_add.py to add servers and their passwords'
print 'PLEASE DO NOT MANUALLY ADD ANYTHING TO servers.txt FILE'
print 'IF YOU WANT TO ADD A SEVER RUN server_add.py'
print 'Install vnstat and enable vnstat on each server'