#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries a given subreddit

    Args:
        subreddit (str): The subreddit to be queried

    Returns:
        int: The number of total subscriber to the subreddit
             0 if not a valid subreddit
    """
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(base_url)
    try:
        no_of_subscribers = response.json().get('data').get('subscribers')
        return no_of_subscribers
    except Exception as e:
        return 0


if __name__ == '__main__':
    number_of_subscribers(subreddit=None)
