#!/usr/bin/python3
"""
Module prints pascal triangle given (n)
"""


def pascal_triangle(n):
    """
    prints pascal's triangle

    Args:
        n: number
    """
    if n < 1:
        return []
 
    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
