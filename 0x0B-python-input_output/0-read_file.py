#!/usr/bin/python3
"""a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """open with"""
    with open(filename, 'r', encoding='utf-8') as op:
        print(op.read(), end="")
