#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = None
    length = len(sentence)
    if len(sentence) == 0:
        return (int(length), first_letter)
    else:
        first_letter = sentence[0]
        return int(length), first_letter
