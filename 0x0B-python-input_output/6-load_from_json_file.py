#!/usr/bin/python3
"""JSON representation"""
import json


def load_from_json_file(filename):
    """function that writes an Object to a text file"""
    with open(filename, encoding='utf-8') as op:
        return(json.loads(op.read()))
