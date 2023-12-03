#!/usr/bin/python3
"""module contain find_peak function"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left_value, right_value = 0, len(list_of_integers) - 1

    while left_value <= right_value:
        middle_value = (left_value + right_value) // 2

        is_peak = (middle_value == 0 or list_of_integers[middle_value - 1] <=
                   list_of_integers[middle_value]) and \
                  (middle_value == len(list_of_integers) - 1 or
                   list_of_integers[middle_value + 1] <=
                   list_of_integers[middle_value])

        if is_peak:
            return list_of_integers[middle_value]

        elif (middle_value > 0 and list_of_integers[middle_value - 1]
              > list_of_integers[middle_value]):
            right_value = middle_value - 1

        else:
            left_value = middle_value + 1

    return None
