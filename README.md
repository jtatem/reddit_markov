Reddit_Markov
=============

Scrapes the front page of a subreddit for comment thread links, then gathers the comments from those.  Feeds the comments into a Markov chain generator.

Markov code is mildly modified from http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/

Later there will probably be a Flask-based interface for this.  Building out capabilities.

reddit_markov.py - This will be the primary interface.  Right now consists of a single function 'markov_subreddit()' which will gather comments and return a Markov object.  Get text by calling generate_markov_text() on the Markov object.

redditfunc.py - Functions for interacting with Reddit

markov.py - Markov class def
