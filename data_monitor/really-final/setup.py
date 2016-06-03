from __future__ import with_statement
import os
import paramiko
import time
from time import sleep
import smtplib
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

with open('servers.txt') as f:
	servers = f.readlines()
for server in servers:
	pswd = server.split(" ",1)[1]
	user = server.split(" ",1)[0]
	ip = user.split("@",1)[1]
	username = user.split("@",1)[0]
	#print ip
	response = os.system("ping -c 1 " + ip+" >/dev/null")
	if response == 0:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(ip, username=username, password=pswd)
		command = 'sudo apt-get install vnstat'
		os.system('echo %s|sudo -S %s' % (pswd, command))
		command = 'sudo vnstat --enable'
		os.system('echo %s|sudo -S %s' % (pswd, command))