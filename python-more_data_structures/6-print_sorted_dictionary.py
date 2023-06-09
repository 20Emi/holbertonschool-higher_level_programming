#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.keys())

    for a in sorted(order):
        print("{} : {}".format(a, a_dictionary.get(a)))
