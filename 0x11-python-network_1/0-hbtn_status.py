#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:\n"
        "\t- type: {}\n"
        "\t- content: {}\n"
        "\t- utf8 content: {}\n"
        .format(type(html), html, html.decode("utf-8")))
