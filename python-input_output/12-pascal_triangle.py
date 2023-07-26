#!/usr/bin/python3
"""
this is a script that returns a list of integers representing pascal's
"""


def pascal_triangle(n):
    """
    prints pascal's triangle
    """
    lists = []
    if n <= 0:
        return lists
    
    lists.append([1])

    for i in range(1, n):
        prev_row = lists[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        lists.append(current_row)

    return lists
