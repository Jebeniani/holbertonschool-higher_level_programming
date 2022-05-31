#!/usr/bin/python3
"""writing to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters"""
    with open('my_first_file.txt', 'w',  encoding='utf-8') as op:
        op.write(text)

    return len(text)
