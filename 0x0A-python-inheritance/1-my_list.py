#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """public instance method"""
        print(sorted(self))
