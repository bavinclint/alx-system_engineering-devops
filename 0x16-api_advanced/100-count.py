#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords"""
from requests import get


def count_words(subreddit, word_list, count_list={}, after=""):
    """"""
    if count_list == {}:
        count_list = {word.lower(): 0 for word in word_list}
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {"User-Agent": "reddit API"}
    data = get(url, headers=headers, allow_redirects=False)
    if data.status_code is not 200:
        return None
    for item in data.json().get('data').get('children'):
        var = item.get('data').get('title')
        for key, value in count_list.items():
            count_list[key] += var.lower().split(' ').count(key)
    after = data.json().get('data').get('after')
    if after is None:
        if all(value == 0 for value in count_list.values()):
            return None
        count_list = sorted(
            count_list.items(),
            key=lambda list: list[1],
            reverse=True)
        for key, value in count_list:
            if value == 0:
                continue
            print("{}: {}".format(key, value))
        return True
    return count_words(subreddit, word_list, count_list, after)
