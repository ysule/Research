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
	filename = "info.txt"
	os.system('rm info-copy.txt')
	os.system('cp info.txt info-copy.txt')
	attachment = open("info-copy.txt", "rb")
					 
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