# code modified from http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/

import random

class Markov(object):
	
	def __init__(self, text):
		self.cache = {}
		self.text = text
		self.words = self.text.split()
		self.word_size = len(self.words)
		self.database()
	
	def triples(self):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""
		
		if len(self.words) < 3:
			return
		
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
			
	def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
				
	def generate_markov_text(self, size=25, seed_word=None):
		seed = random.randint(0, self.word_size-3)
                if seed_word is None:
                    seed_word = self.words[seed]
		    next_word = self.words[seed+1]
		else:
		    try:
		      next_word = self.words[self.words.index(seed_word) + 1]
		    except:
		      next_word = self.words[seed]
		w1, w2 = seed_word, next_word
		gen_words = []
		for i in xrange(size):
	  	    gen_words.append(w1)
		    w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		return ' '.join(gen_words)

     
	def save_text(filename):
	    f = open(filename, 'w')
	    f.write(self.text)
	    f.close()			
