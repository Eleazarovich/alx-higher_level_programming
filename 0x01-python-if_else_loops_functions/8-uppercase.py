#!/usr/bin/python3
def uppercase(str):
    s = list(str)
    for i in range(len(s)):
        if (ord(s[i]) > 96 and ord(s[i]) < 123):
            s[i] = chr(ord(s[i]) - 32)
    print("{}".format(("").join(s)))
