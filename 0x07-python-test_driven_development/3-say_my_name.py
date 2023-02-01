#!/usr/bin/python3
"""
3-say_my_name.py module

the module cointains one function, say_my_name(first_name, last_name)
"""


def say_my_name(first_name, last_name=""):
    """prints my name"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
