#!/usr/bin/python3
"""
this is a script that holds the information of a student
"""


class Student:
    """
    class that holds info bout a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def class_to_json(obj):
    """
    Convert an instance of a Class to a dictionary representation
    """
    loads = self.__dict__
    return loads
