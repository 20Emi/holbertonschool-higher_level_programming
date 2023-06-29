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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """

        jsk = []
        with open(cls.__name__ + ".json", "w") as archivio:

            if list_objs is None:
                archivio.write("[]")
            else:
                for file in list_objs:
                    jsk.append(file.to_dictionary())

                archivio.write(cls.to_json_string(jsk))

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None or len(json_string) == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            manichino = cls(25)  # cls(25) -> per square -- side

        else:
            manichino = cls(25, 25)
            # clase(25, 25)-> per Rectangle - side x width
        manichino.update(**dictionary)

        return manichino
