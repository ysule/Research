import os
with open('links.txt') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    os.system('wget '+line)
