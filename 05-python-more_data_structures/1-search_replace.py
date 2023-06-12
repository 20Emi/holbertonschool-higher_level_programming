#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]

    for a in range(len(my_list)):
        if new[a] == search:
            new[a] = replace
    return new
