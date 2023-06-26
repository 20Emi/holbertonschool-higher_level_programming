#!/usr/bin/python3
"""Task 1"""
from models.base import Base


class Rectangle(Base):
    """In the file models/rectangle.py
    Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
