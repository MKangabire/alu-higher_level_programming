#!/usr/bin/python3
"""
...........''''''
"""


class Student:
    """
    .........
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
        Retrieve a dictionary representation of a Studen
        """
        # If attrs is None, include all attributes
        if attrs is None:
            attrs = self.__dict__.keys()

        # Initialize an empty dictionary to store the JSON representation
        json_dict = {}

        # Loop through the attributes of the instance
        for key, value in self.__dict__.items():
            if key in attrs:
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[key] = value
                elif isinstance(value, (tuple, set)):
                    json_dict[key] = list(value)
                elif isinstance(value, object):
                    json_dict[key] = self.class_to_json(value)

        return json_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based on the

containing attribute names and their corresponding values.
        """
        # Loop through the items in the json dictionary
        for key, value in json.items():
            # Set the attribute with the corresponding value
            setattr(self, key, value)
