import subprocess
import time
import os

start_time = time.time()

while 1:
	proc=subprocess.Popen("who | awk '{print $1}' | sort -u", shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	#print output
	no_users = len(output.split('\n'))-1
	if(no_users == 1):
		current_time = time.time()
		print current_time-start_time
		if(current_time-start_time>10):
			print 'aa'
			#os.system('sudo poweroff')
	if(no_users > 1):
		start_time = time.time()

		

