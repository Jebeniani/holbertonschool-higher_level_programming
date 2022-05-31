#!/usr/bin/python3
"""JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file"""
    with open('filename', 'w') as op:
        json.dump(my_obj, op)
