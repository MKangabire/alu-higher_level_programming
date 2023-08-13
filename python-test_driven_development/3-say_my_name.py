#!/usr/bin/python3
"""
a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    prints the name 
    """
    try:        
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
    except TypeError:
        raise
    else:
         return print("My name is {} {}".format(first_name, last_name)) 
