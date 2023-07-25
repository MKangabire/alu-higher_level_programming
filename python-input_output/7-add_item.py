#!/usr/bin/python3
"""
 a script that adds all arguments to a Python list
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: The object to be saved as JSON.
        filename (str): The name of the JSON file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


def add_items_to_list_and_save(args):
    """
    Add all arguments to a Python list and save them to a JSON file.

    Args:
        args (list): List of arguments.
    """
    # Load existing data from the file (if any)
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    # Append new arguments to the existing data
    existing_data.extend(args)

    # Save the updated data to the file
    save_to_json_file(existing_data, "add_item.json")

if __name__ == "__main__":
    # Exclude the script name from the arguments list
    arguments = sys.argv[1:]
    add_items_to_list_and_save(arguments)
