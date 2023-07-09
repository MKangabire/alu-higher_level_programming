#!/usr/bin/python3
from calculator_1 import *


def main():
    a = 10
    b = 5
    result = add(a, b)
    result2 = sub(a, b)
    result3 = mul(a, b)
    result4 = div(a, b)
    print("{} + {} = {}".format(a, b, result))
    print("{} - {} = {}".format(a, b, result1))
    print("{} * {} = {}".format(a, b, result2))
    print("{} / {} = {}".format(a, b, result3))


if __name__ == "__main__":
    main()
