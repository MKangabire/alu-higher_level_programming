#!/usr/bin/python3
"""
a script that returns true if the object is an instance of the onherited clas
"""


def inherits_from(obj, a_class):
    """
    .......
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
