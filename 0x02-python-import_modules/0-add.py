#!/usr/bin/python3

# program imports addition function involving 2 ints and prints result of a+b


from add_0 import add
if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
