# basic_sororitize
# Author: ILKYU JU ( me [at] ilkyu [dot] kr )

import random
import nltk
from nltk.corpus import names, stopwords, words
import sys

# lists of names from nltk name corpus
random_girl = random.choice(names.words('female.txt'))
random_guy = random.choice(names.words('male.txt'))

# literally lists of phrases that sorority girls love to say
sorority_adverbs = ["literally", "totally", "seriously", "definitely", "kinda"]
sorority_adverbs2 = ["fucking", "goddamn"]
sorority_interjections = ["Oh my gaaahd, "+random_girl + "! ", "O. M. G. Look at her butt. ", "I mean... ", random_girl + "! My cute girl! ", "Waaaaaait. ", "Oh no. ", "Wait. What? ", "Wait. Whaaaaat? "]
sorority_sentences = ['Seriously.', 'Oh wait.', random_girl + ', you are my bestie <3', 'Never mind, I am fine.', 'My heart just stopped for you!', random_girl + ' is such a bitch.', 'Wait, did you see ' + random_girl + '\'s Instagram post?', 'My mom is a total bitch.', "Let's go to Starbucks.", "Eww, " + random_guy + " is so gross.", "Chai tea latte just does not have calories.", "Let me change my political view to vegan.", "I am dating a beta named "+ random_guy + ". He is hot as hell.", "Are we pregaming at " + random_girl +"\'s?", "I am soooooo drunk.", "My iPhone is broken.      oh never mind", random_girl + ", you have to DTR right now."]

# sororitize function
# accepts 
def sororitize(text):
	# POS Tagging the given text
	tokenized = list(filter(None, text.split(' ')))
	pos_tagged = nltk.pos_tag(tokenized)

	# Like, you know, they always start with interjections like "Oh my gaaaahd"
	new_sentence = random.choice(sorority_interjections)
	
	# Now sororitize every word
	for word in pos_tagged:
		# Insert sorority adverbs that modifies verbs (e.g. literally, totally)
		chance = random.randint(1,100)
		startofsentence = False
		endofsentence = False
		nochange = False
		det = False
		if word[1] == 'DT':
			det = True
		if ((word[1] in ['VBP', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] or endofsentence or det) and chance <= 45):
			new_sentence = new_sentence + random.choice(sorority_adverbs) + ' '
		else: nochange = True

		# insert "like, "
		chance = random.randint(1,100)
		if ((word[1]in ['VBP', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']) and chance <= 40):
			new_sentence = new_sentence + "like "
		else: nochange = True

		# insert sorority adverbs that modifies adjectives (e.g. fucking, goddamn)
		if ((word[1] in ['JJ', 'JJS', 'JJR']) and chance <= 25):
			new_sentence = new_sentence + random.choice(sorority_adverbs2) + ' '
		else: nochange = True

		# insert hashtags
		chance = random.randint(1,100)
		if ((word[1]=='NN') and chance <= 35):
			new_sentence = new_sentence + "#"
		else: nochange = True

		# insert space after each word
		if (nochange): 
			new_sentence = new_sentence + word[0]
		new_sentence = new_sentence + ' '

	return new_sentence

if len(sys.argv) == 1:
	print("usage: sororitize.py sentences")
	print("Use quotes (\"\" or \'\') to separate sentences\n")
	# Change the text inside to try other inputs
	sorority = sororitize("I want to get you a chai tea latte to be your best friend. Let's go to Starbucks and have some fun yeaaaah.")
	
	# Insert random phrases after the sororitized text, making the text even more sororitized
	chance = random.randint(1,100)
	if (chance <= 90):
		sorority = sorority + sororitize(random.choice(sorority_sentences))
	
	# Demo: Printing the sororitized sentence
	print (sorority)
	
elif len(sys.argv) > 1:
	for text in sys.argv[1:]:
		print(sororitize(text))