#!/usr/bin/python3
""" script that takes in a URL&email, sends POST request to the passed URL"""
from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = {'email': argv[2]}
    url = argv[1]
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        inf = (response.read()).decode("utf-8")
        print(inf)
