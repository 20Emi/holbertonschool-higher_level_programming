#!/usr/bin/python3
"""Tasks"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """In the file models/square.py
    Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        resul = "[Square] ({}) {}/{} - {}"
        return resul.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
