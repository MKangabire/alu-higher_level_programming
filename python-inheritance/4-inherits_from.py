#!/usr/bin/python3
"""
a python script that returns true if the object is an instance of a class that is inherited
"""


def inherits_from(obj, a_class):
    """
    .......
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
