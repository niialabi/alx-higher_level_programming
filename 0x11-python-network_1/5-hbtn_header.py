#!/usr/bin/python3
"""script takes  URL request URL&displays value of the variable X-Request-Id"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url).headers
    print(r['X-Request-Id'])
