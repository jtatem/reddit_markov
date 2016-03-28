import markov
import redditfunc

def markov_subreddit(subreddit):
    comments = redditfunc.suck_subreddit(subreddit)
    return markov.Markov(' '.join(comments))

def markov_redditor(username, pages=10):
  comments = redditfunc.get_user_comments(username, pages)
  return markov.Markov(' '.join(comments))
