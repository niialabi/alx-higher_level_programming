#!/usr/bin/python3
# program prints argc & argv

from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{(len(argv) - 1)} arguments:")
        j = 1
        for i in range(len(argv)-1):
            print(f"{j}: {argv[j]}")
            j = j + 1
