#!/usr/bin/python3
"""
the object is an instance of a class that inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """returns True if the object"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class:
