#!/usr/bin/python3
"""returns number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """

    headers = {'User-Agent': 'Google Chrome Version 110.0.5481.105'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, headers=headers, timeout=1000)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    return 0
