#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except BaseException as err:
        print(f"Exception: {err}", file=stderr)
        return False
    else:
        return True
