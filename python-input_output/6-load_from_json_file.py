#!/usr/bin/python3
"""
this is a script that creates a object from a“JSON file”
"""


import json


def load_from_json_file(filename):
    """
    json
    """
    with open(filename, mode='r', encoding='utf-8') as myfile:
        folder = json.load(myfile)
        return folder
