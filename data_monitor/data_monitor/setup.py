import os

os.system('sudo pip install paramiko')
os.system('sudo pip install xlwt')
os.system('tar -xzf data_monitor.tar.gz')

print 'Run server_add.py to add servers and their passwords'
print 'PLEASE DO NOT MANUALLY ADD ANYTHING TO servers.txt FILE'
print 'IF YOU WANT TO ADD A SEVER RUN server_add.py'