#!/usr/bin/python3
"""
3-to_json_string.py module
"""
from json import dumps


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return dumps(my_obj)
