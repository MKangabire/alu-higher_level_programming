#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    for i in range(len(my_list)):
        new_elem = my_list[i] * number
        my_list[i] = new_elem
    return my_list
