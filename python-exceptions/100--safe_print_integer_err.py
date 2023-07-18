#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value, end="\n"))
        return True
    except Exception as err_message:
        print("Exception: {}".format(err_message), file=sys.stderr)
        return False
