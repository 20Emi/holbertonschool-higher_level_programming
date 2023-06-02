#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = len(sys.argv)
    if argument == 0:
        print("0 arguments.")
    elif argument == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(argument - 1))
    for a in range(1, argument):
        print("{}: {}".format(a, sys.argv[a]))
