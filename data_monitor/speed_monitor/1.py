import string
with open('/var/log/iptraf/a.log') as f:
	lines = f.readlines()
list = ''
list_m = ''	
for line in lines:
	if 'from 192.168.1.56' in line:
		for s in line.split():
			if s.isdigit():
				if(int(s)>100):
					list = list+ (line.split("to ",1)[1]).split(":",1)[0] + '\n'
					if list.count((line.split("to ",1)[1]).split(":",1)[0]) > 5:
						if((line.split("to ",1)[1]).split(":",1)[0] not in list_m):
							list_m = list_m + (line.split("to ",1)[1]).split(":",1)[0] + '\n'
print list_m