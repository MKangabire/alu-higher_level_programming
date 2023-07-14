#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements1 = set_1.difference(set_2)
    unique_elements2 = set_2.difference(set_1)
    combination = unique_elements1.union(unique_elements2)
    return combination
