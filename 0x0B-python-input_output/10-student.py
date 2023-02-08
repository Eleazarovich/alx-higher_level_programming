#!/usr/bin/python3
"""
10-student.py module

based on 9-student.py
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """etrieves a dictionary representation of a Student"""
        d = {}
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    d.update({i: self.__dict__[i]})
            return d
        return self.__dict__.copy()
