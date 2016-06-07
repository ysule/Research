with open('./universities.txt') as f:
	uni = f.readlines()
for uni in f:
	uni = uni.replace("\n")
	uni = uni.split(",",1)[1]
	uni = uni.split(",",1)[0]
