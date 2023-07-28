#!/usr/bin/python3
"""A python module
that creates an empty
class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
class BaseGeometry():
"""


class Rectangle(BaseGeometry):
    """The class Recatangle that
    inherits the class BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
