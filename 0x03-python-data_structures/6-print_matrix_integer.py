#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for j in matrix:
        for i in j:
            if i == j[-1]:
                print("{:d}".format(i))
            else:
                print("{:d}".format(i), end=" ")
