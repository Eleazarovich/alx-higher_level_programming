#!/usr/bin/python3
from sys import argv

argv_len = (len(argv) - 1)

if argv_len == 0:
    print(argv_len)
else:
    count = 0
    for i in range(1, argv_len+1):
        count += int(argv[i])
    print(count)
