#!/usr/bin/python3
"""
this script appends a string at the end of the text
"""


def append_write(filename="", text=""):
    """
    it adds a string to the file
    """
    with open(filename, mode='a', encoding='utf-8') as myfile:
        file_app = myfile.write(text)
        return file_app
