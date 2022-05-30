#!/usr/bin/python3
"""function checks if the object
is exactly an instance of the specified class"""


def is_kind_of_class(obj, a_class):
    """implentation"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
