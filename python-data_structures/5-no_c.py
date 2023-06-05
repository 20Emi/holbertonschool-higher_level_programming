#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for cat in my_string:
        if cat != "c" and cat != "C":
            str += cat
    return str
