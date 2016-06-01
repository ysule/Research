import os
import time
from time import sleep
os.system('wakeonlan C8:9C:DC:D6:9D:A7 > /dev/null')
print 'Waiting.....'
start = time.time()
while 1:
	sleep(1)
	os.system('ping 192.168.0.196')
	end = time.time()
	if(end-start>20):
		exit()