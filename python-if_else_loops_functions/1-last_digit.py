#!/usr/bin/python3
import random
number = -98


def num(x):
    y = abs(x) % 10
    if (y >= 6):
        print(f"Last digit of {x} is {y} and is greater than 5"
    elif(y == 0):
        print(f"Last digit of {x} is {y} and is 0")
    else:
        y *= -1
        print(f"Las t digit of {x} is {y} and is less than 6 and not 0")
num(number)
