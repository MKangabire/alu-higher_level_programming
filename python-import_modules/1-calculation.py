#!/usr/bin/python3
from calculator_1 import *


def main():
    a = 10
    b = 5
    result = a + b
    result1 = a - b
    result2 = a * b
    result3 = a / b
    print("{} + {} = {}".format(a, b, result))
    print("{} - {} = {}".format(a, b, result1))
    print("{} * {} = {}".format(a, b, result2))
    print("{} / {} = {}".format(a, b, result3))


if __name__ = "__main__":
    main()
