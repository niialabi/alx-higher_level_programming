#!/usr/bin/python3
def uppercase(str):
    for i in str:
        asc = int(ord(i))
        if asc >= 97 and asc <= 122:
            asc = asc - 32
        else:
            asc = asc
        print(chr(asc), end="")
    print()
