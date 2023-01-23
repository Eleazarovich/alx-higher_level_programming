#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        print(f"Exception: {err}", file=stderr)
    finally:
        return result
