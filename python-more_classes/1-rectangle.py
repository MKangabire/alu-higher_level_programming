#!/usr/bin/python3
"""
This is a python script that
creates a class with attributes
and method.
"""


class Rectangle:
    """
    this is a class that
    has private instance atrributes,
    getters, and setters, and a method
    for initialization.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

     def get_width(self):
         return self.__width

     def get_height(self):
         return self.__height
