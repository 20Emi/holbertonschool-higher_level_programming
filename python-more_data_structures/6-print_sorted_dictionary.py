#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.keys())
    order.sort()  # Sorts the list items into place

    for a in order:
        print("{} : {}".format(a, a_dictionary.get(a)))
