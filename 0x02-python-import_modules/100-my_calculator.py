#!/usr/bin/python3
# calculator that handles basic operations +/-/*/_/_
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    # add
    if argv[2] == "+":
        print(f"{a} + {b} = {add(a, b)}")
    # subtraction
    if argv[2] == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    # multiplication
    if argv[2] == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    # division
    if argv[2] == "/":
        print(f"{a} / {b} = {div(a, b)}")
