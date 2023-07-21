#!/usr/bin/python3
"""
this is a code that checks if the size is an integer
"""


class Square:
    """
    class for squares
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
