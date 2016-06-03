import string
with open('/home/praneeth/Desktop/test.log') as f:
	lines = f.readlines()
for line in lines:
	if 'from 192.168.1.56' in line:
		print line