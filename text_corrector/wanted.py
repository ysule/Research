from collections import OrderedDict
with open('./uni_words.txt') as f:
	uni = f.readlines()
x = ''
uni = str(uni).replace("\n","")

o1 = open("./wanted.txt","a")
print len(uni)
uni = "".join(OrderedDict.fromkeys(uni))
print(uni)
if é in uni:
	print 'aww'
"""
o1.write('\n'+x)
o1.close()
"""