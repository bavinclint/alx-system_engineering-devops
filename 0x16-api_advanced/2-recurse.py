#!/usr/bin/python3
"""
    script that queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
"""


import requests


base_url = 'https://www.reddit.com/'


def recurse(subreddit, hot_list=[], after=""):
    """
        return a list containing the titles of all hot articles for a given
        subreddit
    """

    try:
        if after is None:
            return

        response = requests.get(
            url="{}/r/{}/hot.json".format(base_url, subreddit),
            headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
            params={'after': after}
        )

        data = response.json()['data']
        after = data['after']

        for child in data['children']:
            hot_list.append(child['data']['title'])

        recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
