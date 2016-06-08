def corrector(line, wanted):
	x = ''
	for character in line:
		if character not in wanted:
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
				if word in 'aAiI,.oO':
					x = x +' ' + word
				else:
					word = ''
			else:
				x = x + ' ' + word
	print x
#wanted = raw_input("not wanted:")
with open('./wanted.txt') as file:
	wanted=file.read().replace('\n', '')+' '
while 1:
	corrector(raw_input("line: "), wanted)
