import string
import getpass
import base64
x = 1
while 1:
	if(x==1):
		user_name = raw_input("Enter username:")
		ip = raw_input("Enter server ip:")
		print("Enter your password(THIS WILL BE ENCRYPTED")
		password = getpass.getpass()
		print("Enter password second time")
		password_1 = getpass.getpass()
		if(password==password_1):
			result = ''
			for i in range(0, len(password)):
				result = result + chr(ord(password[i]) - 2)
			print 'Your password is encrypted!!'
			print 'Your encrypted password is'
			output = open("servers.txt","a")
			server = user_name+'@'+ip+' '+result
			print server
			output.write(server+"\n")
			output.close
			output.flush()
		else:
			print"Sorry!!, your passwords didn't match"
		x = raw_input("Press 1 to continue: ")
		x = int(x)
	else:
		exit()