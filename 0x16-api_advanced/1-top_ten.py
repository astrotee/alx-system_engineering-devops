#!/usr/bin/python3
""" query the reddit API """
import requests


def top_ten(subreddit):
    """ query the top hot posts of a subreddit """
    headers = {'User-Agent': 'linux:testapp.01'}
    r = requests.get(f' https://www.reddit.com/r/{subreddit}/hot.json?limit=9',
                     headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    for post in r.json()['data']['children']:
        print(post['data']['title'])
