import requests
import time
import re
from BeautifulSoup import BeautifulSoup, SoupStrainer
import HTMLParser
import markov

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}

def get_frontpage_links(subreddit):
    url = 'https://www.reddit.com/r/{0}'.format(subreddit)
    r = requests.get(url, allow_redirects=False, headers=headers)
    thread_links = list(set([link.get('href') for link in BeautifulSoup(r.text, parseOnlyThese=SoupStrainer('a')) if link.has_key('href') and 'comments' in link.get('href')]))
    return thread_links

def get_thread_comments(thread_url):
    r = requests.get(thread_url, allow_redirects=False, headers=headers)
    s = BeautifulSoup(r.text, convertEntities=BeautifulSoup.HTML_ENTITIES)
    divs = s.findAll('div', {'class': 'md'})
    comments = [re.sub('<[^<]+?>', '', str(d).split('<p>')[1].split('</p>')[0].replace('\n', ' ')) for d in divs if '<p>' in str(d)][1:]
    return comments 

def get_user_comments(user, max_pages=5):
    first_page_url = 'https://www.reddit.com/user/{0}'.format(user)
    print('Fetching up to {0} pages of comments for user {1}'.format(max_pages, user))
    print('Fetching URL {0}'.format(first_page_url))
    r = requests.get(first_page_url, headers=headers)
    s = BeautifulSoup(r.text, convertEntities=BeautifulSoup.HTML_ENTITIES)
    divs = s.findAll('div', {'class': 'md'})
    comments = [re.sub('<[^<]+?>', '', str(d).split('<p>')[1].split('</p>')[0].replace('\n', ' ')) for d in divs if '<p>' in str(d)]
    pagecount = 1
    finished = False
    while not finished and pagecount < max_pages:
      nextpagelink = [link.get('href') for link in BeautifulSoup(r.text, parseOnlyThese=SoupStrainer('a')) if link.has_key('href') and 'after' in link.get('href') and 'count={0}'.format(pagecount * 25) in link.get('href')]
      if len(nextpagelink) == 0:
        finished = True
      else:
        pagecount += 1
        nextpagelink = str(nextpagelink[0])
        print('Fetching URL {0}'.format(nextpagelink))
        r = requests.get(nextpagelink, headers=headers)
        s = BeautifulSoup(r.text, convertEntities=BeautifulSoup.HTML_ENTITIES)
	divs = s.findAll('div', {'class': 'md'})
        comments += [re.sub('<[^<]+?>', '', str(d).split('<p>')[1].split('</p>')[0].replace('\n', ' ')) for d in divs if '<p>' in str(d)]
    return comments
      

def suck_subreddit(subreddit):
    threads = get_frontpage_links(subreddit)
    print('Found {0} threads for /r/{1}'.format(len(threads), subreddit))
    comments = []
    for thread in threads:
        if not thread.startswith('http'):
            url = 'https://www.reddit.com{0}'.format(thread)
        else:
            url = thread
	print('Fetching thread URL {0}'.format(url))
	comments += get_thread_comments(url)
        time.sleep(1)
    return comments

