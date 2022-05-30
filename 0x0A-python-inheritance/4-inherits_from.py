#!/usr/bin/python3


def inherits_from(obj, a_class):
    """function checks if the object
    is exactly an instance of a class that inherited"""

    if type(obj) != a_class:
        return True
    else:
        return False
