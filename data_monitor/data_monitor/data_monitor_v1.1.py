#Author: Bedapudi Praneeth
#Set a cron job for this script
#Install vnstat on each server before you add it to servers.txt and enable vnstat
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
#Reading server information from text file
date_old = '00/00/00'
while 1:
	if(time.strftime("%x")>date_old):
		date_old = time.strftime("%x")
		down = str(datetime.date.today())
		with open('servers.txt') as f:
			servers = f.readlines()
		for server in servers:
			#As each server info is in new line, when Python reads the info "\n" is also present. So we need to remove it.
			server = server.replace("\n", "")
			#print server
			#As defined password is in on right to " " and username is left to "@" and ip is between "@" and " "
			pswd = server.split(" ",1)[1]
			user = server.split(" ",1)[0]
			ip = user.split("@",1)[1]
			username = user.split("@",1)[0]
			result = ''
			for i in range(0, len(pswd)):
				result = result + chr(ord(pswd[i]) + 2) 
			pswd = result
			response = os.system("ping -c 1 " + ip+" >/dev/null")
			if response == 0:
				try:
					#connecting to server using ssh and reading output of command vnstat -d
					client = paramiko.SSHClient()
					client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					client.connect(ip, username=username, password=pswd)
					stdin, stdout, stderr = client.exec_command('vnstat -d')
					stdin_h, stdout_h, stderr_h = client.exec_command('hostname')
					x =''
					for line in stdout:
						x = x+line
					for l in stdout_h:
						l = l.replace("\n", "")
					#Latest day's information is always the 3rd line from last.
					data = x.splitlines()[-3].encode('utf-8')
					data =ip+'    '+l+ data.replace("|", "")

					#print data
					output = open("info.txt","a")
					#Writing data to text file
					output.write(data+"\n")
					output.close
					#VERY VERY VERY IMPORTANT. UNLESS YOU DO THIS, CHANGES TO FILE WON'T BE SAVED UNTIL AFTER SCRIPT COMPLETES EXECUTION AND OLD VERSION OF FILE WILL BE MAILED
					output.flush()
				except:
					down = down+'    '+ip
					o1 = open("down.txt","a")
					o1.write(down+"\n")
					o1.close
					o1.flush()
			else:
				down = down+'    '+ip
				o2 = open("down.txt","a")
				o2.write(down+"\n")
				o2.close
				o2.flush()
		#Converting text file to Excel sheet
		data = []
		with open("info.txt") as f:
			for line in f:
				data.append([word for word in line.split("  ") if word])
		#print data
		wb = xlwt.Workbook()
		sheet = wb.add_sheet("Info")
		for row_index in range(len(data)):
			for col_index in range(len(data[row_index])):
				sheet.write(row_index, col_index, data[row_index][col_index])
		data = []
		with open("down.txt") as f:
			for line in f:
				data.append([word for word in line.split("  ") if word])
		sheet = wb.add_sheet("Down")
		for row_index in range(len(data)):
			for col_index in range(len(data[row_index])):
				sheet.write(row_index, col_index, data[row_index][col_index])
		wb.save("info.xls")

		#Mailing
		fromaddr = "serverstatus@app.innoplexus.de"
		#toaddr = ["suyash.masugade@innoplexus.com","bedapudi.praneeth@innoplexus.com"]
		toaddr = ["bedapudi.praneeth@innoplexus.com"]
		for t in toaddr:
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = t
			msg['Subject'] = "data usage log attached"			 
			body = "The following servers are unreachable (This means that the script was unable to SSH into the following servers for whatever the reason)" +'\n'+ down			 
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
			#print'Mails sent!!'