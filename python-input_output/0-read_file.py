#!/usr/bin/python3
"""
this a python script that reads a file
"""


def read_file(filename=""):
    """
    it reads and printsthe content of a file
    """
    with open(filename, mode='r', encoding='utf-8') as myfile:
        content = myfile.read()
        print(content, end="")
