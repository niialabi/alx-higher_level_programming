#!/usr/bin/python3
"""script that takes your GitHub credentials uses the GitHubAPI disp id"""

from sys import argv
import requests

if __name__ == "__main__":
    u_name = argv[1]
    u_token = argv[2]
    resp = r = requests.get(f'https://api.github.com/users/{u_name}', headers={"Authorization": f'{u_token}'})
    print(resp.json().get('id'))
