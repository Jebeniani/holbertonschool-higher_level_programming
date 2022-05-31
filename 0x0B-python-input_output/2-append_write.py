#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """ a function that appends a string at the end of a text file
    and returns the number of characters added"""
    with open('file_append.txt', 'a', encoding='utf-8') as op:
        return (op.write(text))

