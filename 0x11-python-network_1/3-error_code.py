#!/usr/bin/python3
""" script that takes URL, sends a request to URL&displays body of response"""
from sys import argv
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print((response.read()).decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.status}')
