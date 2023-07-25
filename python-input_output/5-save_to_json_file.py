#!/usr/bin/python3
"""
this is a script that writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    json
    """
    with open(filename, mode='w', encoding='utf-8') as myfile:
        return json.dump(my_obj, myfile)
