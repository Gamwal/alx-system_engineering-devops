#!/usr/bin/python3
"""
Recursive function that queries the Reddit
API and returns a list containing the titles
of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function that queries a subreddit

    Args:
        subreddit (str): The subreddit to be queried
        hot_list (list): list to store titles

    Returns:
        list: List of all hot topics in subreddit
              None if not a valid subreddit
    """

    base_url = "https://www.reddit.com/r/{}/hot.json"\
        .format(subreddit)
    headers = {'User-agent': 'yourbot'}
    params = {'after': after} if after else {}
    response = requests.get(base_url, headers=headers,
                            params=params, allow_redirects=False)

    try:
        response_list = response.json().get('data').get('children')
        hot_list.extend([i.get('data').get('title') for i in response_list])

        after = response.json().get('data').get('after')

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception as e:
        return None


if __name__ == '__main__':
    recurse(subreddit='Programming')
