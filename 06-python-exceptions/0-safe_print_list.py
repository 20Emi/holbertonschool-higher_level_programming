#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    saf = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            saf += 1
        except Exception:
            break
    print()
    return saf
