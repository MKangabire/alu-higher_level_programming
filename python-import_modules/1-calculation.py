#!/usr/bin/python3
from calculator_1 import *
a = 10
b = 5
result = add(a, b)
result1 = sub(a, b)
result2 = mul(a, b)
result3 = div(a, b)
print("{} + {} = {}".format(a, b, result))
print("{} - {} = {}".format(a, b, result1))
print("{} * {} = {}".format(a, b, result2))
print("{} / {} = {}".format(a, b, result3))
