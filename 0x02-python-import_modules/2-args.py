#!/usr/bin/python3
from sys import argv

argv_len = (len(argv) - 1)

if argv_len == 0:
    print(f"{argv_len} arguments.")
elif argv_len == 1:
    print(f"{argv_len} argument:")
    print(argv[argv_len])
else:
    print(f"{argv_len} arguments:")
    for i in range(argv_len):
        print(f"{i+1}: {argv[i+1]}")
