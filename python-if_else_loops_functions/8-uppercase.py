#!/usr/bin/python3
def uppercase(string):
    upper_string = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_string += "{}".format(chr(ord(char) - 32))
        else:
            upper_string += "{}".format(char)
    print("{}".format(upper_string))
