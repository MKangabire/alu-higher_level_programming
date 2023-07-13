#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = sentence[0]
    length = len(sentence)
    if len(sentence) == 0:
        first_letter == None
        return (int(length), first_letter)
    else:
       return (int(length), first_letter)
