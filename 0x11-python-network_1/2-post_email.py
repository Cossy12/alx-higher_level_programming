#!/usr/bin/python3
"""
URL and  email, sends a POST to the requested
 email as the parameter and displays  response
"""
import sys
import urllib.request
import urllib.parse
if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    params = urllib.parse.urlencode(val).encode('ascii')
    req = urllib.request.Request(url, params)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
