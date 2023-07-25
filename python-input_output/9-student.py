#!/usr/bin/python3
"""
this is a script that holds the information of a student
"""


class Student:
    """
    class that holds info bout a student
    """
    def __init__(self, first_name, last_name, age):
        self.name1 = first_name
        self.name2 = last_name
        self.age = age

def class_to_json(obj):
    """
    Convert an instance of a Class to a dictionary representation
"""
    json_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
        elif isinstance(value, (tuple, set)):
            json_dict[key] = list(value)
        elif isinstance(value, object):
            json_dict[key] = class_to_json(value)

    return json_dict

