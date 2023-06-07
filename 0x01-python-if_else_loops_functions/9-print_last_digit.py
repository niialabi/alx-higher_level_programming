#!/usr/bin/python3
# function prints last digit of number
def print_last_digit(number):
    absolute_number = abs(number)
    output = absolute_number % 10
    print(output, end="")
    return output
