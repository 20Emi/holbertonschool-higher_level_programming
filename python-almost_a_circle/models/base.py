#!/usr/bin/python3
"""Task 1"""
import json


class Base:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)
