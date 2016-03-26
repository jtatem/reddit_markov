Reddit_Markov
=============

Scrapes the front page of a subreddit for comment thread links, then gathers the comments from those.  Feeds the comments into a Markov chain generator.

Markov code is mildly modified from http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/

Later there will probably be a Flask-based interface for this.  Building out capabilities.

Files
-----

reddit_markov.py - This will be the primary interface.  Right now consists of a single function 'markov_subreddit()' which will gather comments and return a Markov object.  Get text by calling generate_markov_text() on the Markov object.

redditfunc.py - Functions for interacting with Reddit

markov.py - Markov class def

Example
-------

All subject to change.

python -i reddit_markov.py

>>> m = markov_subreddit('askreddit')
Found 52 threads for /r/askreddit
Fetching thread URL https://www.reddit.com/r/AskReddit/comments/4bx577/dd_players_what_have_been_some_of_your_favourite/
Fetching thread URL https://www.reddit.com/r/AskReddit/comments/4bw721/what_is_the_biggest_unanswered_question_from_your/
[...more urls, this will go to a debug log later...]
>>> m.generate_markov_text()
'on to us (furniture, good clothing and toys, Ukrainian literature). Even at a bicycle shop and learned Tagalog, but them knowing English was a straight male.'
>>> m.generate_markov_text(seed_word='batman')
"Batman at the fact that we have to flee for so long until your horde becomes it's own arm for a year off doing various jobs."
>>> m.generate_markov_text(seed_word='europe')
"Europe has had 3 since birth, and another one or two then it just wouldn't show anything. I have almost all of this? I have security."
>>> m.generate_markov_text(seed_word='moon', size=20)
'Moon has some pretty sophisticated tracking and control abilities. That is an amazing experience and life continues without us. A by'
>>> gen = m.textgenerator(seed_word='man', req_punct=True)
>>> gen.next()
"man who knew this fact but I don't know how to get closer. My mom is from A.A. Lewis. You didn't see anyone. I went war."
>>> gen.next()
'man /r/unexpectedfactorial This would give me heart disease, and hurt everybody around me, while giving myself cancer! Sounds great! The feeling of independence, freedom, being etc.'



