#install vnstat before doing all this
from __future__ import with_statement
import os
import paramiko
import time
from time import sleep
import smtplib
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
	print ip
	response = os.system("ping -c 1 " + ip+" >/dev/null")
	if response == 0:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(ip, username=username, password=pswd)
		stdin, stdout, stderr = client.exec_command('vnstat -d')
		line_no = 1
		for line in stdout:
			if line_no == 6:
				output = open("monitor.txt","a")
				output.write(ip+"	"+line)
				output.close
			line_no = line_no+1
	else:
		print server, 'is down'
fromaddr = "serverstatus@app.innoplexus.de"
#toaddr = ["suyash.masugade@innoplexus.com","bedapudi.praneeth@innoplexus.com"]
toaddr = ["bedapudi.praneeth@innoplexus.com"]
for t in toaddr:
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = t
	msg['Subject'] = "data usage log"			 
	body = "data usage log attached"					 
	msg.attach(MIMEText(body, 'plain'))					 
	filename = "monitor.txt"
	attachment = open("monitor.txt", "rb")
					 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
					 
	msg.attach(part)
					
	server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com:587')
	server.starttls()
	server.login("AKIAJLVT63DSM247NJHQ", "AvAqwJImHHr9Ow98fImQo9E4GvI73WiKQgsSKAGfId70")
	text = msg.as_string()
	server.sendmail(fromaddr, t, text)
	server.quit()
	print'Mails sent!!'