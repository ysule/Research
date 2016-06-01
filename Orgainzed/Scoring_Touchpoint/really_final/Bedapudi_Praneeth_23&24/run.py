import os
import glob
with open('config.txt') as f:
    content = f.readlines()
"""
i=0
while i<len(content):
	print content[i]
	i = i+1
"""
filenames = glob.glob('*.py')
i=0
while i<len(filenames):
	match = filenames[i][:1]
	j=0
	while j<len(content):
		match_c = content[j][:1]
		if match == match_c:
			os.system ("python "+filenames[i]+" "+content[j][2:])
		j = j+1
        i = i+1
