import smtplib
from random import randint
fromaddr = 'praneethbedapudi@gmail.com'
toaddrs  = 'bedapudi.praneeth@innoplexus.com'

otp_number = randint(10000,99999)

msg = "\r\n".join([
  "From: praneethbedapudi@gmail.com",
  "To: bedapudi.praneeth@gmail.com",
  "Subject: Hello",
  "",
  str(otp_number)
  ])

username = 'praneethbedapudi@gmail.com'
password = 'rao!pravam3'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()