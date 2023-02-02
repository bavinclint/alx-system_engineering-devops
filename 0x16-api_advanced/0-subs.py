#!/usr/bin/python3
"""
    script that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
"""


import requests


base_url = 'https://www.reddit.com/'


def number_of_subscribers(subreddit):
    """
        return the number of subscribers
    """

    try:
        response = requests.get(
            url="{}/r/{}/about.json".format(base_url, subreddit),
            headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
        )

        data = response.json()['data']

        return data['subscribers']
    except Exception:
        return False
