#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# convert number to absolute number to get correct output
absolute_last_digit = abs(number) % 10
# changing print out format if negative / positive
if number < 0:
    output = "Last digit of {} is -{} and is {}"
else:
    output = "Last digit of {} is {} and is {}"
# properly formating output
if absolute_last_digit > 5:
    print(output.format(number, absolute_last_digit, "greater than 5"))
elif absolute_last_digit == 0:
    print(output.format(number, absolute_last_digit, 0))
elif (absolute_last_digit > 0) and (absolute_last_digit < 6):
    print(output.format(number, absolute_last_digit, "less than 6 and not 0"))
