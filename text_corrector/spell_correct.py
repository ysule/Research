import re, collections
import time
import string
def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
		model = collections.defaultdict(lambda: 1)
		for f in features:
				model[f] += 1
		return model

NWORDS = train(words(file('big.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
	
def edits1(word):
	 splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	 deletes    = [a + b[1:] for a, b in splits if b]
	 transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	 replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	 inserts    = [a + c + b     for a, b in splits for c in alphabet]
	 return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
		return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
		candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
		return max(candidates, key=NWORDS.get)
while 1:
	text = raw_input("Enter:")
	t1 = time.time()
	for old in ('/',';',';','\\'):
		text = text.replace(old, '')
	words = text.split()
	a = ''

	for word in words:
		if(len(word)==1):
			if word in ('a','A','i','I',',','.'):
				a = a + word
			else:
				word = ''
		else:
			if word[-1:] in (',', '.', '"',):
				a = a + ' '+ correct(word[:-1]) + word[-1:]
			else:
				if word[:1] in (',', '.', '"',):
					a = a + ' ' + word[:1]+ correct(word[1:])
				else:
					a = a + ' '+ correct(word)

	t = time.time() - t1
	print t
	print a