#!/usr/bin/python3
"""task 2"""


class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):
        """size must be >= 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
