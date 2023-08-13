#!/usr/bin/python3
"""Module to find the max integer in a list
"""

ValueToSmallError = __import__('value_to_small').ValueToSmallError


def max_integer(list_data=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    try:
        if not isinstance(list_data, list):
            raise TypeError("Arguement should be of Datatype list")
        elif len(list_data) == 0:
            return None
        for value_type in list_data:
            if type(value_type) is not int:
                raise TypeError(f"value {value_type} not of data type int")
            else:
                continue
        if len(list_data) < 2:
            return list_data[len(list_data) - 1]
        result = list_data[0]
        i = 1
        while i < len(list_data):
            if list_data[i] > result:
                result = list_data[i]
            i += 1
        return result
    except TypeError:
        raise
