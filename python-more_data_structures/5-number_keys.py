#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    keyss = list(a_dictionary.keys())

    for a in keyss:
        number += 1

    return number
