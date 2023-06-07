#!/usr/bin/python3
def uppercase(str):
    for i in str:
        asc = int(ord(i))
        if asc >= 97 and asc <= 122:
            asc = chr(asc - 32)
        else:
            asc = chr(asc)
        print("{}".format(asc), end='')
    print()
