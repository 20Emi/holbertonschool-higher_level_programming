#!/usr/bin/python3
"""Task 1"""


class MyList(list):
    """class MyList that inherits from list:
    * prints the list, but sorted"""

    def print_sorted(self):

        print(sorted(self))
