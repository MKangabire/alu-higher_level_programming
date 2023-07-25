#!/usr/bin/python3
"""
this a pythohon script that reads a file
"""


def read_file(filename=""):
    """
    it reads a file
    """
    with open(filename, mode='r', encoding='utf-8') as myfile:
        print(myfile.read())
