#!/usr/bin/python3
"""task 4"""


def print_square(size):
    """ function that prints a square with the character #."""

    for a in range(size):
        if not isinstance(size, int) and size < 0:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        for j in range(size):
            print("#", end="")
        print()
