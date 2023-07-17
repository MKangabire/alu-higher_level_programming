#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sublist in matrix:
        new_list = []
        for element in sublist:
            new_element = element**2
            new_list.append(new_element)
        new_matrix.append(new_list)
    return new_matrix
