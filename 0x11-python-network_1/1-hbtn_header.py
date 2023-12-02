#!/usr/bin/python3
"""
 send  request to  URL and displays
  value of the X-Request-Id variable 
"""
from sys import argv
import urllib.request
if __name__ == "__main__":
    quest = urllib.request.Request(argv[1])
    with urllib.request.urlopen(quest) as response:
        print(dict(response.headers).get("X-Request-Id"))
