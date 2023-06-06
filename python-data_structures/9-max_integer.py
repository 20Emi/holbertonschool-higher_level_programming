#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = my_list[0]

    if len(my_list) == 0:
        "None"

    for a in range(len(my_list)):
        if mx < my_list[a]:
            mx = my_list[a]
    return mx
