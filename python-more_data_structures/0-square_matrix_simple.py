#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix=[]
    for sublist in matrix:
        new_list = (element**2 for element in sublist)
        new_matrix.append(new_list)
    return new_matrix
