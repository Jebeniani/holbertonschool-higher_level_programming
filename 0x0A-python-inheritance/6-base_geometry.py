#!/usr/bin/python3
"""Public instance method that raises an Exception
with the message area() is not implemented"""


class BaseGeometry:
    def area(self):
        """implementation"""
        raise Exception("area() is not implemented")
