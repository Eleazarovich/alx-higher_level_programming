#!/bin/usr/python3
"""Base module"""
import json
from os import path
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}", mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances (convert json representations)"""
        file_load = "{}.json".format(cls.__name__)
        if not path.isfile(file_load):
            return []
        with open(file_load, "r", encoding="utf-8") as f:
            return[cls.create(**dic) for dic in cls.from_json_string(f.read())]
