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

# In the next iteration, the raw input needs to be changed to permit an input that is based on another input.
# It is likely that the input will be collected from a Gizmodo article, as the articles will change periodically and give the bot some variability.
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