#!/usr/bin/python3
"""
e a function that prints a text with 2 new lines after each of these character
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        i = 0
        new_string = ""
        while i < len(text):
            if text[i] in ['?', '.', ':']:
                new_string += text[i]
                new_string += "\n\n"
                if i < len(text) - 1 and text[i + 1] == " ":
                    i += 1
                    while text[i] == " ":
                        i += 1
                elif i < len(text) - 1 and text[i + 1] != " ":
                    i += 1
            else:
                new_string += text[i]
                i += 1
        return print(new_string, end="")
    except TypeError:
        raise
