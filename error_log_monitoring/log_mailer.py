import time
from time import sleep
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

while 1:
	with open('/var/log/nginx/error.log') as f:
		sum_old = sum(1 for _ in f)
	sleep(1)
	with open('/var/log/nginx/error.log') as f_new:
		sum_new = sum(1 for _ in f_new)
	#if(sum_new>=sum_old):
	if(sum_new>sum_old):
		fromaddr = "praneethbedapudi@gmail.com"
		toaddr = "bedapudi.praneeth@innoplexus.com"
		 
		msg = MIMEMultipart()
		 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "error log"
		 
		body = "error log attached"
		 
		msg.attach(MIMEText(body, 'plain'))
		 
		filename = "error.log"
		attachment = open("/var/log/nginx/error.log", "rb")
		 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		 
		msg.attach(part)
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "rao!pravam3")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print'Mail sent!!'