#!/usr/bin/env python
import smtplib
import os
from random import randint
fromaddr = 'praneethbedapudi@gmail.com'
toaddrs  = 'bedapudi.praneeth@innoplexus.com'

otp_number = randint(10000,99999)
print otp_number
msg = "\r\n".join([
  "From: praneethbedapudi@gmail.com",
  "To: bedapudi.praneeth@gmail.com",
  "Subject: Hello",
  "",
  str(otp_number)
  ])
print 0
username = 'praneethbedapudi@gmail.com'
password = 'rao!pravam3'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
print 1
server.starttls()
print 2
server.login(username,password)
print 3
server.sendmail(fromaddr, toaddrs, msg)
print 4
server.quit()
print 5
