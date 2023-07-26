#!/usr/bin/python3
"""
this is a script hecks if the width and height
"""


class BaseGeometry:
    """
    this is a class
    """
    def integer_validator(self, value):
        try:
            int_value = int(value)
            return True
        except ValueError:
            return False


class Rectangle(BaseGeometry):
    """
    .........
    """
    def __init__(self, width, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if self.integer_validator(width) and self.integer_validator(height):
            if width > 0 and height > 0:
                self.__width = width
                self.__height = height
            else:
                raise ValueError("width must be greater than 0")
