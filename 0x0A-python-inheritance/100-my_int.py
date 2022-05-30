#!/usr/bin/python3


class MyInt(int):
    """Creating a class named MyInt"""
    def __init__(self, value):
        """initialising MyINt"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.value = value

    def __eq__(self, val):
        """the equal method"""
        return (str(self.value) == str(val))

    def __ne__(self, val):
        """the not equal method"""
        return (str(self.value) != str(val))
