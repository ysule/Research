import string
import getpass
import base64
x = 1
key = raw_input("Enter encryption code: ")
o = open("secret.txt","a")
key = str(key)
o.write(key)
o.close
while 1:
	if(x==1):
		user_name = raw_input("Enter username:")
		ip = raw_input("Enter server ip:")
		print("Enter your password(THIS WILL BE ENCRYPTED")
		password = getpass.getpass()
		print("Enter password second time")
		password_1 = getpass.getpass()
		if(password==password_1):
			enc = []
			for i in range(len(password)):
				key_c = key[i % len(key)]
				enc_c = chr((ord(password[i]) + ord(key_c)) % 256)
				enc.append(enc_c)
			print base64.urlsafe_b64encode("".join(enc))
			print encoded
			print 'Your password is encrypted!!'
			print 'Your encrypted password is'
			print password
		else:
			print"Sorry!!, your passwords didn't match"
		x = raw_input("Press 1 to continue: ")
		x = int(x)
	else:
		exit()