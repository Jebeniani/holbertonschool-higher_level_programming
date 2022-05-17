#!/usr/bin/python3
""" Creating an empty class named Square.
"""


class Square:
    """ Size being a private instance attribute.
    """
    def __init__(self, size):
        """ Instantiation with size
        """
        self.__size = size
