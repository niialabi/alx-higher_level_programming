#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request"""
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) == 1:
        q = {'q': ''}
    else:
        q = {'q': argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', q)
    try:
        jresp = r.json()
        if jresp:
            print(f'[{jresp["id"]}] {jresp["name"]}')
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
