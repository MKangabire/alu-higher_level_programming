#!/usr/bin/python3
"""
this is a python script that overwrites in a file when it is available
"""


def write_file(filename="", text=""):
    """
    it overwrites on the content found in the existing file
    """
    with open(filename, mode='w', encoding='utf-8') as myfile:
        new_file = myfile.write(text)
        return new_file
