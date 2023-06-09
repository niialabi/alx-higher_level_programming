#!/usr/bin/python3
# program prints argc & argv

from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0: arguments.")
    else:
        print(f"{(len(argv) - 1)} argument:")
        j = 1
        for i in range(len(argv)-1):
            print(f"{j}: {argv[j]}")
            j = j + 1
