#run setup.py everytime you add a new server
from __future__ import with_statement
import os
import paramiko
import time
import xlwt
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
	server = server.replace("\n", "")
	print server
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
		stdin, stdout, stderr = client.exec_command('vnstat -d')
		x =''
		for line in stdout:
			x = x+line
		data = x.splitlines()[-3].encode('utf-8')
		data =ip+ data.replace("|", "")
		print data
		output = open("info.txt","a")
		output.write(data+"\n")
		output.close
		#VERY VERY VERY IMPORTANT. UNLESS YOU DO THIS, CHANGES TO FILE WON'T BE SAVED UNTIL AFTER SCRIPT COMPLETES EXECUTION AND OLD VERSION OF FILE WILL BE MAILED
		output.flush()
	else:
		down = ''
		down = down+ip

data = []
with open("info.txt") as f:
	for line in f:
		data.append([word for word in line.split("  ") if word])
print data
wb = xlwt.Workbook()
sheet = wb.add_sheet("New Sheet")
for row_index in range(len(data)):
	for col_index in range(len(data[row_index])):
		sheet.write(row_index, col_index, data[row_index][col_index])
wb.save("info.xls")

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
	filename = "info.xls"
	attachment = open("info.xls", "rb")
					 
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