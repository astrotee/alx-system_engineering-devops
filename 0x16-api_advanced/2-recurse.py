#!/usr/bin/python3
""" query the reddit API """
import requests as req


def recurse(subreddit, hot_list=[], after=''):
    """ query all hot posts of a subreddit """
    base_url = 'https://www.reddit.com'
    headers = {'User-Agent': 'linux:testapp.01'}
    r = req.get(f'{base_url}/r/{subreddit}/hot.json?after={after}&limit=100',
                headers=headers, allow_redirects=False)
    if r.status_code != 200 and len(hot_list) == 0:
        return None
    data = r.json()
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])
    if data['data']['after'] is None:
        return hot_list
    return recurse(subreddit, hot_list, data['data']['after'])
