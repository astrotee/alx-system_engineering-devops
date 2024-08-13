#!/usr/bin/python3
""" query the number of subscribers of a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ query the number of subscribers of a subreddit """
    headers = {'User-Agent': 'linux:testapp.01'}
    r = requests.get(f' https://www.reddit.com/r/{subreddit}/about.json',
                     headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    return r.json()['data']['subscribers']
