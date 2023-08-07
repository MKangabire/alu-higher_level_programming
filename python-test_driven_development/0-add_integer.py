#!/usr/bin/python3
"""
a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    adds 2 integers
    """
    if not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    results = sum(a, b)
    return results
