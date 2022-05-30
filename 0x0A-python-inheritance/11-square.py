#!/usr/bin/python3
"""writing a class named Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creating a class Square from class Rectangle
    """
    def __init__(self, size):
        """initialising with size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
