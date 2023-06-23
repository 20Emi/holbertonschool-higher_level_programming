#!/usr/bin/python3
"""task 4"""


def print_square(size):
    """ function that prints a square with the character #."""

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        for j in range(size):
            print("#", end="")
        print()
