#!/usr/bin/python3
""" Creating an empty class named rectangle.
"""


class Rectangle:
    """define a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")

        myRect = ""
        for i in range(self.__height):
            myRect += "#" * self.__width

            if i + 1 < self.__height:
                myRect += "\n"

        return myRect

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width is not an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height is not an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)

        return perimeter
