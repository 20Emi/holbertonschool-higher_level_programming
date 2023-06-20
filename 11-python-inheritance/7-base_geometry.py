#!/usr/bin/python3
"""Task 7"""


class BaseGeometry:
    """ that raises an Exception with the message
    * if value is not an integer: raise a TypeError
    * if value is less or equal to 0: raise a ValueError"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
