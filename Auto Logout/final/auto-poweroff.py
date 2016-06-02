import time
import subprocess
from time import sleep
import os

start_time = time.time()

while 1:
	#All the usernames which are currently logged in can be seen with who | awk '{print $1}' | sort -u
	#usin subprocess because we need to count the number of lines in terminal output
        proc=subprocess.Popen("who | awk '{print $1}' | sort -u", shell=True, stdout=subprocess.PIPE, )
        output=proc.communicate()[0]
    #As each user's name appears in new line with one extra line at the start, number of users = number of lines in output-1
        no_users = len(output.split('\n'))-1
    #If no one is logged in then number of users is 0
        if(no_users < 1):
        	#If no one is logged in timer starts.
        	#current_time-start_time gives the number of seconds elapsed since last user logged out
                current_time = time.time()
            #1200 = 20 minutes. change it to your suitable value
                if(current_time-start_time>1200):
            #admin password is needed to poweroff the server.
            #change admin123 to sudo password of server.
            #Storing the admin password may be a bad idea. Use encryption and decryption for this. (May be?)
                        sudoPassword = 'admin123'
                        command = 'poweroff'
                        os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        else:
        	#Start time needs to be the time when number of users becomes zero
                start_time = time.time()