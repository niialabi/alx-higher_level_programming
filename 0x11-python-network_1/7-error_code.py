#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
