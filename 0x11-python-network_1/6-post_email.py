#!/usr/bin/python3
"""
email submit and post
"""
import requests
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
