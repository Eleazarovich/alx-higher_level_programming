#!/usr/bin/python3
"""
4-from_json_string.py module
"""
from json import loads


def from_json_string(my_str):
    """returns an object (data structure) represented by a JSON string"""
    return loads(my_str)
