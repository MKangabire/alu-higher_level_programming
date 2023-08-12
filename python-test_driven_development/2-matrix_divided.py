#!/usr/bin/python3
"""
a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides the elements of the matrix with the div
    """
    if not isinstance(matrix, list) or (
        not all(isinstance(row, list) and
                all(isinstance(element, (int, float))
                    for element in row)
                for row in matrix)):
            raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
