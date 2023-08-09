#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries a given subreddit to get top ten posts

    Args:
        subreddit (str): The subreddit to be queried

    Returns:
        str: The number of total subscriber to the subreddit
             None if not a valid subreddit
    """

    base_url = "https://www.reddit.com/r/{}/hot.json?limit=10"\
        .format(subreddit)
    response = requests.get(base_url, allow_redirects=False)
    try:
        for i in response.json().get('data').get('children'):
            print(i.get('data').get('title'))
    except Exception as e:
        return None


if __name__ == '__main__':
    top_ten(subreddit=None)
