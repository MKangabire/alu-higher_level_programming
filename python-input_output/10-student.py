#!/usr/bin/python3
"""
.....
"""


class Student:
    """
    ............
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()

        json_dict = {}
        for key, value in self.__dict__.items():

            if key in attrs:
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[key] = value
                elif isinstance(value, (tuple, set)):
                    json_dict[key] = list(value)
                elif isinstance(value, object):
                    json_dict[key] = self.class_to_json(value)

        return json_dict

