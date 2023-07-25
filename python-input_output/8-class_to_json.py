#!/usr/bin/python3
"""
a script that returns the dict description with simple data structure
"""


def class_to_json(obj):
    """
    Convert an instance of a Class to a dictionary representation suitable for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representation of the object suitable for JSON serialization.
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

