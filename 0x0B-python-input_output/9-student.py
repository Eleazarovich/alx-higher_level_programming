#!/usr/bin/python3
"""
9-student.py module
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """etrieves a dictionary representation of a Student"""
        return self.__dict__
