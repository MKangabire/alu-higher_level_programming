#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)
    if length_a == 0 or length_b == 0:
        if length_a == 0 and length_b == 0:
            tuple_a = (0, 0)
            tuple_b = (0, 0)
        elif length_a == 0:
            tuple_a = (0, 0)
        else:
            tuple_b = (0, 0)
    elif length_a == 1 or length_b == 1:
        if length_a == 1 and length_b == 1:
            tuple_a = (tuple_a[0], 0)
            tuple_b = (tuple_b[0], 0)
        elif length_a == 1:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_b = (tuple_b[0], 0)
    else:
        if length_a > 2 and length_b > 2:
            tuple_a = (tuple_a[0], tuple_a[1])
            tuple_b = (tuple_b[0], tuple_b[1])
        elif length_a == 0:
            tuple_a = (tuple_a[0], tuple_a[1])
        else:
            tuple_b = (tuple_b[0], tuple_b[1])
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
