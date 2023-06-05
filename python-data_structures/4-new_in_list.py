#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx >= 0 and len(my_list) > idx:
        copy = my_list.copy()
        copy[idx] = element
        return copy
    else:
        return my_list
