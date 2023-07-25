#!/usr/bin/python3
"""Script to gather data from an API"""

import requests
import sys


def make_requests(num):
    """
    Function that prints out details realting to an employee's tasks

    Args:
        num: The employee ID
    """
    
    if len(sys.argv) != 2:
        return

    try:
        num = int(num[1])
    except Exception as e:
        return

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos/'
                       .format(num))
    req1 = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(num))

    count = len([i for i in req.json() if i.get('completed') is True])

    print("Employee {} is done with tasks({}/{}):"
          .format(req1.json().get('name'), count, len(req.json())))

    for i in req.json():
        if i.get('completed') is True:
            print("\t{}".format(i.get('title')))


if __name__ == "__main__":
    make_requests(sys.argv)
