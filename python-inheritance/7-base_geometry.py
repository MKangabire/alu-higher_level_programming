#!/usr/bin/python3
"""
a python script that raises an error if the value is not an integer
"""


class BaseGeometry:
    """
    ...........
    """
    def __init__(self, do_print=False):
        if do_print:
            self.count = 1

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        self.value = value
