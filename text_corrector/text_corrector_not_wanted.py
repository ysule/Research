def corrector(line, not_wanted):
	x = ''
	for character in line:
		if character in not_wanted:
			character = ''
		else:
			x = x + character
	words = x.split()
	x = ''
	for word in words:
		letter_count = 0
		for letter in word:
			if letter in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890':
				letter_count = letter_count + 1
		if letter_count > (len(word)/2): 
			if(len(word) == 1):
				if word in 'aAiI,.':
					x = x +' ' + word
				else:
					word = ''
			else:
				x = x + ' ' + word
	print x
#not_wanted = raw_input("not wanted:")
#not_wanted = '~`!@#$%^&*()_+=[]{}\\/'
with open('./not_wanted.txt') as file:
	not_wanted=file.read().replace('\n', '')
while 1:
	corrector(raw_input("line: "), not_wanted)