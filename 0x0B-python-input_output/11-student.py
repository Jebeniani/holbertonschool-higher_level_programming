#!/usr/bin/python3
"""writing a class named Student"""


class Student:
    """creating the class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json method that retrieves
        a dictionary representation of a Student instance"""
        dict = {}
        if type(attrs) is not list:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    dict[i] = self.__dict__[i]
            return(dict)

    def reload_from_json(self, json):
        """json method that replaces all attributes of the Student instance"""
        for i in json:
            self.__dict__[i] = json[i]
