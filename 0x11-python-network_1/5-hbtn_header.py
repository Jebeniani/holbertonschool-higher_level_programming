#!/usr/bin/python3
"""Python script that takes in a URL
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    value = response.headers.get('X-Request-Id')
    print(value)
