#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def num(x):
    y = abs(x) % 10 
    if x < 0:
        y *= -1
    if (y >= 6):
        print(f"Last digit of {x} is {y} and is greater than 5")
    elif(y == 0):
        print(f"Last digit of {x} is {y} and is 0")
    else:
        print(f"Las t digit of {x} is {y} and is less than 6 and not 0")
num(number)
