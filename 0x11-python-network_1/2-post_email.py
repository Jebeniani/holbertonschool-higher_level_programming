#!/usr/bin/python3
"""Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    val = urllib.parse.urlencode({"email": argv[2]}).encode('ascii')
    req = urllib.request.Request(argv[1], val)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
