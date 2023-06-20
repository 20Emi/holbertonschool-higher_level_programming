#!/usr/bin/python3
"""Task 7"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by
    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangle__width = width
        self._Rectangle__height = height
