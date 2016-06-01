from __future__ import with_statement
import time
from time import sleep
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


with open('/var/log/nginx/error.log') as f:
		sum_start = sum(1 for _ in f)
while 1:
	with open('/var/log/nginx/error.log') as f:
		sum_now = sum(1 for _ in f)
		f.seek (0, 2)           # Seek @ EOF
		fsize = f.tell()        # Get Size
		f.seek (max (fsize-1024, 0), 0) # Set pos @ las
		lines = f.readlines()
	if(sum_now > sum_start):
		find_str = "[error]"
		count = sum_now - sum_start
		lines = lines[-count:]
		for line in lines:
			print line
			if find_str in line:
				fromaddr = "serverstatus@app.innoplexus.de"
				toaddr = ["suyash.masugade@innoplexus.com","bedapudi.praneeth@innoplexus.com"]
				for t in toaddr:
					msg = MIMEMultipart()
					 
					msg['From'] = fromaddr
					msg['To'] = t
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
					
					server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com:587')
					server.starttls()
					server.login("AKIAJLVT63DSM247NJHQ", "AvAqwJImHHr9Ow98fImQo9E4GvI73WiKQgsSKAGfId70")
					text = msg.as_string()
					server.sendmail(fromaddr, t, text)
					server.quit()
				print'Mails sent!!'
				sum_start = sum_now