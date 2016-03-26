import markov
import redditfunc

def markov_subreddit(subreddit):
    comments = redditfunc.suck_subreddit(subreddit)
    return markov.Markov(' '.join(comments))
