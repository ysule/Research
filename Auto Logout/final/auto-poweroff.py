import time
import subprocess
from time import sleep
import os

start_time = time.time()

while 1:
        proc=subprocess.Popen("who | awk '{print $1}' | sort -u", shell=True, stdout=subprocess.PIPE, )
        output=proc.communicate()[0]
        #print output
        no_users = len(output.split('\n'))-1
        if(no_users < 1):
                current_time = time.time()
                #print current_time-start_time
                if(current_time-start_time>1200):
                        sudoPassword = 'admin123'
                        command = 'poweroff'
                        os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        else:
                start_time = time.time()