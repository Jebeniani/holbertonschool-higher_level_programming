#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ returns True if the object
    is an instance of a class that
    inherited from the specified class ; otherwise False. """

    if type(obj) is not a_class:
        return True
    else:
        return False
