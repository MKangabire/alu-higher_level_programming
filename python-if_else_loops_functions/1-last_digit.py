#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def num(x):
    y = x % 10
    if y >= 6:
        print(f"Last digit of {x} is {y} and is greater than 5" )
    elif( y == 0):
        print(f"Last digit of {x} is {y} and is 0")
    else:
        print(f"Last digit of {x} is {y} and is less than 5 and not 0" )
num(number)
