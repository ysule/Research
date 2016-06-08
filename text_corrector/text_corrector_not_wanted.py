def corrector(line, not_wanted):
	corrected_line = ''
	for character in line:
		if character in not_wanted:
			character = ''
		else:
			corrected_line = corrected_line + character
	words = corrected_line.split()
	corrected_line = ''
	for word in words:
		letter_count = 0
		for letter in word:
			if letter in 'qwertyuiopasdfghjklzcorrected_linecvbnmQWERTYUIOPASDFGHJKLZcorrected_lineCVBNM1234567890':
				letter_count = letter_count + 1
		if letter_count > (len(word)/2):
			if len(word) == 1:
				if word in 'aAiI,.':
					corrected_line = corrected_line +' ' + word
				else:
					word = ''
			else:
				corrected_line = corrected_line + ' ' + word
	print corrected_line
#not_wanted = raw_input("not wanted:")
#not_wanted = '~`!@#$%^&*()_+=[]{}\\/'
with open('./not_wanted.txt') as Myfile:
	not_wanted_list = Myfile.read().replace('\n', '')
while 1:
	corrector(raw_input("line: "), not_wanted_list)
