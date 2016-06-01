#Make changes to mac address and ip
import os
import time
from time import sleep
start = time.time()
while 1:
	os.system('wakeonlan C8:9C:DC:D6:9D:A7 > /dev/null')
	print 'Waiting.....'
	sleep(1)
	os.system('ssh nikhil.fulzele@192.168.0.196')
	end = time.time()
	if(end-start>20):
		exit()