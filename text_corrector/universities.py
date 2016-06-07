with open('./universities.txt') as f:
	uni = f.readlines()
for u in uni:
	u = u.replace("\n","")
	u = u.split(",",1)[1]
	u = u.split(",",1)[0]
	words = u.split()
	for word in words:
		o1 = open("./uni_words.txt","a")
		o1.write(word+"\n")
		o1.close