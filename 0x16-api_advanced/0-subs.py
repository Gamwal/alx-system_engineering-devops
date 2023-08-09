#!/usr/bin/python3
""""""

import requests


def number_of_subscribers(subreddit):
    """"""
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(base_url)
    no_of_subscribers = response.json().get('data').get('subscribers')
    print(no_of_subscribers)
    return no_of_subscribers


if __name__ == '__main__':
    number_of_subscribers(subreddit=None)
