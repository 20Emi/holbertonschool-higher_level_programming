#!/usr/bin/python3
"""Task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """*size must be private. No getter or setter
    *size must be a positive integer, validated by integer_validator
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self._Rectangle__size = size

    def area(self):
        return self._Rectangle__size * self._Rectangle__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(
            self._Rectangle__size, self._Rectangle__size)
