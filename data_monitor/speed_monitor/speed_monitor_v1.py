from __future__ import with_statement
import os
import paramiko
import time
import datetime
import xlwt
from time import sleep
import smtplib
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

date_old = time.strftime("%x")
while 1:
	date_now = time.strftime("%x")
	name = date_now + '.log'
	name = string.replace(name, '/', '-')
	command = 'sudo iptraf -i all -L ./'+name+'-t 1430 -B'
	os.system(command)
	delete_command_txt = 'find . -name "*.txt" -type f -delete'
	delete_command_xls = 'find . -name "*.xls" -type f -delete'
	os.system(delete_command_txt)
	os.system(delete_command_xls)
	h = 0
	#list_m_old = ''
	while 1:
		with open('./'+name) as f:
			lines = f.readlines()
		list = ''
		repeat = ''
		list_m = ''	
		for line in lines:
			if 'from 192.168.1.56' in line:
				for s in line.split():
					if s.isdigit():
						if(int(s)>100):
							list = list+ (line.split("to ",1)[1]).split(":",1)[0] + '\n'
							if list.count((line.split("to ",1)[1]).split(":",1)[0]) > 5:
								if((line.split("to ",1)[1]).split(":",1)[0] not in list_m):
									list_m = list_m + (line.split("to ",1)[1]).split(":",1)[0] + '\n'
		"""
		for i in list_m:
			if i in list_m_old:
				repeat = repeat + i
				print 'found 1'
			else:
				print 'nope'
		print 'repeat:'
		print repeat
		print 'all:'
		print list_m
		list_m_old = list_m
		"""
		name1 = str(h)+'.txt'
		os.system('touch '+name1)
		o = open(name1,"a")
		o.write(list_m)
		o.close
		o.flush()

		data = []
		with open(name1) as f:
			for line in f:
				data.append([word for word in line.split("  ") if word])
		#print data
		wb = xlwt.Workbook()
		sheet = wb.add_sheet("Info")
		for row_index in range(len(data)):
			for col_index in range(len(data[row_index])):
				sheet.write(row_index, col_index, data[row_index][col_index])
		wb.save(str(h)+".xls")
		#Mailing
		fromaddr = "serverstatus@app.innoplexus.de"
		#toaddr = ["suyash.masugade@innoplexus.com","bedapudi.praneeth@innoplexus.com"]
		toaddr = ["bedapudi.praneeth@innoplexus.com"]
		for t in toaddr:
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = t
			msg['Subject'] = "IP addresses attached"			 
			body = 'IP addresses attached'			 
			msg.attach(MIMEText(body, 'plain'))					 
			filename = str(h)+".xls"
			attachment = open(str(h)+".xls", "rb")
							 
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

		if(time.strftime("%x")>date_old):
			date_old = date_now
			break
		h = h+1
		sleep(3590)