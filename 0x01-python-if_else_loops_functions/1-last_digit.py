#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute_last_digit = number % 10
if number < 0:
    last_digit = -absolute_last_digit
else:
    last_digit = absolute_last_digit
output = "Last digit of {} is {} and is {}"

if absolute_last_digit > 5:
    print(output.format(number, last_digit, "greater than 5"))
elif absolute_last_digit == 0:
    print(output.format(number, last_digit, 0))
elif (absolute_last_digit >= 0) and (absolute_last_digit < 6):
    print(output.format(number, last_digit, "less than 6 and not 0"))
