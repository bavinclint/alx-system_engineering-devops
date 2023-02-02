#!/usr/bin/python3
"""
    script that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
"""


import requests


base_url = 'https://www.reddit.com/'


def top_ten(subreddit):
    """
        return the number of subscribers
    """

    try:
        response = requests.get(
            url="{}/r/{}/hot.json?limit=10".format(base_url, subreddit),
            headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
        )

        data = response.json()['data']

        for child in data['children']:
            print(child['data']['title'])
    except Exception:
        print(None)
