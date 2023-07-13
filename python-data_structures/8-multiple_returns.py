#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter =  sentence[0]
    length = len(sentence)
    if sentence == 0:
        sentence[0] == None
    else:
       print("{:d}, {}".format(ord(first_letter), length))
