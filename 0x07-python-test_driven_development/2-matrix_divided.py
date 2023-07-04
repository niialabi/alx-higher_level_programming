#!/usr/bin/python3
""" Module that divides all elements of matrix by value """
def matrix_divided(matrix, div):
    """ Function that divides all alements in a matrix by "div"

    Args:
        matrix (list of lists): matrix containing int/float
	div (int/float): number to divide individual elements of matrix by

    Return:
        Returns new matrix with divided elemnts
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(ele, list) for ele in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix)
    collum_len = len (matrix[0])
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
           raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for x in matrix:
        new_row = []
        for y in x:
            new_row.append(round((y / 3), 2))
        new_matrix.append(new_row)
    return (new_matrix)
