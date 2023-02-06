#!/usr/bin/python3
"""
1-my_list.py module

the module contains one class, MyList
"""


class MyList(list):
    """MyList inherits from list"""
    def print_sorted(self):
        """prints the list in asceding order"""
        print(sorted(self))
