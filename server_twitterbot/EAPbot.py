#!/usr/local/bin/python2.7

import pickle, random
from tweepy import API, OAuthHandler, Cursor
import requests
from bs4 import BeautifulSoup 
import EAPkey


a = open('/home/gileshc/twitterbot/lexicon-EAP', 'rb')
successorlist = pickle.load(a)
a.close()

f = requests.get('http://gizmodo.com').text
soup = BeautifulSoup(f)
start_words = []
counter = 0

def nextword(a):
	if a in successorlist:
		return random.choice(successorlist[a])
	else: 
		return 'the'

# Generate the list of words in start_words.
for p in soup.find_all('p'):
    for s in p:
        tst = []
        try:
            tst = [w for w in s.string.decode('unicode_escape').encode('ascii', 'ignore').split() if len(w)>4]
        except:
            pass
        if len(tst)>10:
            for w in tst: 
                start_words.append(w)
    if len(start_words) > 150:
        break

speech = ''

ckey = EAPkey.keychain('ckey')
skey = EAPkey.keychain('skey')
token = EAPkey.keychain('token')
stoken = EAPkey.keychain('stoken')

auth = OAuthHandler(ckey, skey)
auth.set_access_token(token, stoken)

api = API(auth)

# In the next iteration, the raw input needs to be changed to permit an input that is based on another input.
# It is likely that the input will be collected from a Gizmodo article, as the articles will change periodically and give the bot some variability.

# This loop will run up to 3 times.
while counter < random.randint(1,2):
	counter += 1
	speech = random.choice(start_words)
	s = random.choice(speech.split())
	response = speech + ''

	while True:
		
		# If the word introduces an error, it will be replaced with a common word, 'bird'.
		try:
			neword = nextword(s)
		except:
			neword = nextword('bird')
		
		# make sure that the generated text is no longer than 140 characters
		if len(response) >= 140:
			break
		response += ' ' + neword
		s = neword
		if neword[-1] in ',?!.:|':
			break
	
	bot_talk = response
	
	# If the message is not longer than 140 characters, post it. 
	if len(bot_talk) <= 140:
		api.update_status(status=bot_talk)
