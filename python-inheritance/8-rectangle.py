#!/usr/bin/python3
"""
this is a script hecks if the width and height
"""


class BaseGeometry:
    """
    ...........
    """
    def integer_validator(self, value):
        try:
            int_value = int(value)
            return True
        except ValueError:
            return False


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if self.integer_validator(width) and self.integer_validator(height):
            if width > 0 and height > 0:
                self.__width = width
                self.__height = height
            else:
                raise ValueError("Width and height must be positive integers")
        else:
            raise ValueError("Width and height must be positive integers")

