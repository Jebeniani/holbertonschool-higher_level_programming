#!/usr/bin/python3
"""Python script that takes your GitHub credentials
and uses the GitHub API to display your id"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get('https://api.github.com/user', auth=(argv[1],
        argv[2])).json().get('id')

    print(req)
