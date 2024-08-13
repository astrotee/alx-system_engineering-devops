#!/usr/bin/python3
""" query the reddit API """
import requests as req


def count_words(subreddit, word_list, fq={}, after=''):
    """ count kewords in post titles of a subreddit """
    base_url = 'https://www.reddit.com'
    headers = {'User-Agent': 'linux:testapp.01'}
    r = req.get(f'{base_url}/r/{subreddit}/hot.json?after={after}&limit=100',
                headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return
    data = r.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        unique_words = {w.lower() for w in word_list}
        for word in unique_words:
            fq[word] = fq.get(word, 0) + title.split().count(word)
    if data['data']['after'] is None:
        for word, n in sorted(fq.items(), key=lambda x: (x[1], x[0]),
                              reverse=True):
            if n == 0:
                continue
            print(f'{word}: {n}')
        return
    return count_words(subreddit, word_list, fq, data['data']['after'])
