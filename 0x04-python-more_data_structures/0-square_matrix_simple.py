#!/usr/bin/python3
# row loops throug various row in matrix
# at same time row is an anonymos function that squares every element in itself
def square_matrix_simple(matrix=[]):
    # square = lambda x: x * x
    # row = lambda rows: list(map(square, rows))

    new_list = list(map(lambda rows: list(map(lambda x: x * x, rows)), matrix))
    return (new_list)
