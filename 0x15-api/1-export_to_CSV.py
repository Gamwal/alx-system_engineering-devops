#!/usr/bin/python3
"""Script to gather data from an API and export to CSV"""

import csv
import requests
import sys


def make_requests(num):
    """
    Function that writes details of an employee's tasks to csv file

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
    filename = "{}.csv".format(num)

    with open(filename, 'w') as f:
        for i in req.json():
            data = [i.get('userId'), req1.json().get('username'),
                    i.get('completed'), i.get('title')]
            data = f'"{data[0]}","{data[1]}","{data[2]}","{data[3]}"\n'
            f.write(data)


if __name__ == "__main__":
    make_requests(sys.argv)
