#!/usr/bin/python3
"""
a python script that raises an error if the value is not an integer
"""


class BaseGeometry:
    """
    ...........
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validation(self, name, vale):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")