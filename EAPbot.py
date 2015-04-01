import pickle, random
a = open('lexicon-EAP', 'rb')
successorlist = pickle.load(a)
a.close()

def nextword(a):
	if a in successorlist:
		return random.choice(successorlist[a])
	else: 
		return 'the'

speech = ''

while speech != 'quit':
	speech = raw_input('>')
	s = random.choice(speech.split())
	response = speech + ''

	while True:
		# If the word introduces an error, it will be replaced with a common word, 'bird'.
		try:
			neword = nextword(s)
		except:
			neword = nextword('bird')
		response += ' ' + neword
		s = neword
		if neword[-1] in ',?!.':
			break
	print response