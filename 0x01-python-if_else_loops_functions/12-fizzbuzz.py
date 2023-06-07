#!/usr/bin/python3
# generate numbers separated by space
for i in range(1, 101):
    # check if multiple of 3 & 5 //if yes implement fizzbuzz
    if i % 3 == 0 or i % 5 == 0:
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end=" ")
# check if multiple of 3 //if yes implement fizz
        elif i % 3 == 0:
            print("Fizz", end=" ")
# check if multiple of 5 // if yes implement buzz
        elif i % 5 == 0:
            print("Buzz", end=" ")
# else print number
    else:
        print(i, end=" ")
print()
