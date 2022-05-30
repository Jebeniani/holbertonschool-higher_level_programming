#!/usr/bin/python3
"""wrintig a class named Square
that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creating Square class"""
    def __init__(self, size):
        """initializer of class attributes"""
        self.integer_validator("self", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """area 51"""
        return (self.__size ** 2)
