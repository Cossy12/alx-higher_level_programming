#!/usr/bin/python3
""" commits from  recent to the oldest
of the repository  user rails
"""
from sys import argv
import requests
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get('commit').get('author').get('name'))
