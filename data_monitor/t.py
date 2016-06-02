#install vnstat before doing all this
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
		stdin, stdout, stderr = client.exec_command('vnstat -i wlan0 --oneline')
		line_no = 1
		for line in stdout:
			line = line.encode('utf-8')
			s = line.split(';')
			total =';'.join(s[14:])
			total_out = ';'.join(s[13:])
			s1 = total_out.split(';')
			total_out = ';'.join(s1[:1])
			total_in = ';'.join(s[12:])
			s2 = total_in.split(';')
			total_in = ';'.join(s2[:1])
			print total_in
			print total_out
			print total
	else:
		print server, 'is down'