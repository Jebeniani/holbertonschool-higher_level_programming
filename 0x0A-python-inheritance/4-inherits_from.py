#!/usr/bin/python3
"""function checks if the object
is exactly an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """implentation"""
    if type(obj) != a_class:
        return True
    else:
        return False
