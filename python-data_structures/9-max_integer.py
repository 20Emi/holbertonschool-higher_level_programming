#!/usr/bin/python3
def max_integer(my_list=[]):
    
    if my_list == 0:
        "None"
    mx = my_list[0]
    for a in range(len(my_list)):
        if mx < my_list[a]:
            mx = my_list[a]
    return mx
