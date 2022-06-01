#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file
    after each line containing a specific string"""
    new = ""
    with open(filename, 'r+', encoding='utf-8') as op:
        for line in op:
            new += line
            if search_string in line:
                new += new_string
        op.seek(0)
        op.write(new)
