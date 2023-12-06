#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    r = requests.get(url)
    r = requests.post(url, email)
    print(r.text)
