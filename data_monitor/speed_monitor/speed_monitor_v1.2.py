from __future__ import with_statement
import os
import paramiko
import time
import datetime
import xlwt
from time import sleep
import netifaces as ni
import smtplib
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#While deploying on server comment or change the following line to server's ip
from_ip = '192.168.1.56'
#While deploying on server change eth0 in the following line to whatever the interface name is and uncomment it
#from_ip = ni.ifaddresses('eth0')[2][0]['addr']
statement = 'from ' + from_ip
date_old = time.strftime("%x")
while 1:
	date_now = time.strftime("%x")
	#creating new log for each day
	name = date_now + '.log'
	name = string.replace(name, '/', '-')
	#os.system('rm ./'+name)
	os.system('touch ./'+name)
	command = 'sudo iptraf -i all -L ./'+name+'-t 1430 -B'
	#command = 'sudo iptraf -i all -L ./'+name+' -B'
	os.system(command)
	time_old = int(time.strftime('%X')[:2]) - 1
	#list_m_old = ''
	while 1:
		if int(time.strftime('%X')[:2])>time_old:
			h = int(time.strftime('%X')[:2])
			time_old = h
			with open('./'+name) as f:
				lines = f.readlines()
			#print lines
			list = ''
			repeat = ''
			list_m = ''
			print statement
			for line in lines:
				if statement in line:
					for s in line.split():
						if s.isdigit():
			#While deploying change 100 in the following line to minimum thershold value
							if(int(s)>100):
								print s
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
			#print 'list'
			#print list_m
			#Mailing
			fromaddr = "serverstatus@app.innoplexus.de"
			toaddr = ["suyash.masugade@innoplexus.com","bedapudi.praneeth@innoplexus.com","pradumna.panditrao@innoplexus.com"]
			#toaddr = ["bedapudi.praneeth@innoplexus.com"]
			for t in toaddr:
				msg = MIMEMultipart()
				msg['From'] = fromaddr
				msg['To'] = t
				msg['Subject'] = statement + ' till ' + str(h) + ' :00' + ' time'
				body = list_m
				msg.attach(MIMEText(body, 'plain'))
				filename = str(h)+".xls"
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
