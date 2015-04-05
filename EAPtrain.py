# GeekyAllanPoe trainer
import requests
from bs4 import BeautifulSoup
import pickle

# First collect some tech writing.
link = 'http://gizmodo.com'

gawker = requests.get(link)
gawker = gawker.text 
sopa = BeautifulSoup(gawker)

links = []

#Locate the links in sopa
s = sopa.find_all('h1')
for item in s:
	links.append(item.find('a').get('href'))

with open('techtext.txt', 'wb') as txt:

	for link in links:
		url = link
		url = requests.get(url)
		url = url.text
		soup = BeautifulSoup(url)
		a_text = ""

		for p in soup.find_all('p'):
			for s in p:
				try:
					# Note that the decode() and encode() functions at the end will get rid of the unicode characters that are causing problems.
					for st in s.string.lstrip().rstrip().lower().replace("|", " ").replace(":"," ").decode('unicode_escape').encode('ascii', 'ignore'):
						a_text += st
				except:
					pass
		
		# Write the text content of the current page to techtext.txt
		txt.write(a_text)
		txt.write('\n')

# Next, create a list of all the words in the order they appear in both texts.
eap = open('EAP_raven.txt')
giz = open('techtext.txt')
text = []
for f in [giz, eap]:
	for line in f:
		for word in line.lstrip().split():
			text.append(word)
eap.close()
giz.close()

textset = list(set(text))
follow = {}
for l in range(len(textset)):
	working = []
	check = textset[l] 
	for w in range(len(text)-1):
		if check == text[w] and text[w][-1] not in '(),.!|':
			working.append(str(text[w+1]))
		follow[check] = working
a = open('lexicon-EAP', 'w')
pickle.dump(follow, a, 2)
a.close()