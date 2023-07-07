#!/usr/bin/python3
import random
number = random.randint(-10, 10)
def num(x):
    if (x<0):
        print(x, "is negative")
    elif(x == 0):
        print(x, "is zero")
    else:
        print(x, "is positive")
num(number)
