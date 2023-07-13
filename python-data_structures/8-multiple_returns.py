#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = sentence[0]
    length = len(sentence)
    if len(sentence) == 0:
        if first_letter is None:
        return (int(length), first_letter)
    else:
       return int(length),first_letter
