#!/usr/bin/python3
"""
class inheriting from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    ....
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validation(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_negative(self, name, value):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >=0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def validation(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_negative(self, name, value):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >=0")
