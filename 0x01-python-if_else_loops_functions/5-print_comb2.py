#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        print("{num:02d}, ".format(num=i), end="")
    else:
        print(i)
