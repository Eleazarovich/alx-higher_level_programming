#!/usr/bin/python3
"""
101-locked_class.py module

the module cointains one class, LockedClass
"""


class LockedClass:
    """
    prevents the user from dynamically creating a new instance attributes,
    except if the new instance attribute is called first_name
    """
    __slots__ = ["first_name"]
