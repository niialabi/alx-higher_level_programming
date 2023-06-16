#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for i, j in a_dictionary.items():
        b_dictionary[i] = (2 * j)
    return b_dictionary
