#!/usr/bin/python3
"""Tasks"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """In the file models/square.py
    Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
