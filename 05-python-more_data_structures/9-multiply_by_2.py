#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_directory = a_dictionary.copy()
    new_directory.items()

    for a in new_directory:
        new_directory[a] *= 2

    return new_directory
