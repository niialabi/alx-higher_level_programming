#!/usr/bin/python3
# program sums up all the args

from sys import argv
if __name__ == "__main__":
    _sum = 0
    j = 1
    for i in range(len(argv) - 1):
        _sum = _sum + int(argv[j])
        j = j + 1
    print(_sum)
