#!/usr/bin/python3
"""script takes  URL request URL&displays value of the variable X-Request-Id"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1]).headers
    print(r['X-Request-Id'])
