#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = sentence[0]
    length = len(sentence)
    if len(sentence) == 0:
        return None
    else:
       return (int(length), first_letter)
