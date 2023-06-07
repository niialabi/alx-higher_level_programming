#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            if 89 != (j + 10 * i):
                print('{:02d}'.format(j + 10 * i), end=", ")
            else:
                print("89")
