#!/usr/bin/python3
"""
..................
"""


class BaseGeometry:
    def integer_validator(self, value):
        """
        Validate if the given value is an integer.

        Args:
            value (int): The value to be validated.

        Returns:
            bool: True if the value is an integer, False otherwise.
        """
        try:
            int_value = int(value)
            return True
        except ValueError:
            return False


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer.
        """
        if self.integer_validator(width) and self.integer_validator(height):
            if width > 0 and height > 0:
                self.__width = width
                self.__height = height
            else:
                raise ValueError("Width and height must be positive integers")
        else:
            raise ValueError("Width and height must be positive integers")

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        if self.integer_validator(size):
            if size > 0:
                super().__init__(size, size)
            else:
                raise ValueError("Size must be a positive integer")
        else:
            raise ValueError("Size must be a positive integer")

