#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode="r", encoding="UTF8") as f:
        print(f.read(), end="")
