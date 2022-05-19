#!/usr/bin/python3
"""Square class
Defines a square class
and has private instance size
"""


class Square:
    """Square class
    TypeError exception with the message size must be an integer
    """
    def __init__(self, size=0):
        """__init__
        initializing square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """area
        returns area of square
        """
        return self.__size * self.__size
