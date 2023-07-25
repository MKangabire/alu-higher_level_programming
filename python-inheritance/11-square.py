#!/usr/bin/python3
"""
..............
"""


class BaseGeometry:
    """
    ...............
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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    def __init__(self, size):
        if self.integer_validator(size):
            if size > 0:
                super().__init__(size, size)
            else:
                raise ValueError("Size must be a positive integer")
        else:
            raise ValueError("Size must be a positive integer")

    def __str__(self):
        return f"[Square] {self.__width}/{self.__height}"

