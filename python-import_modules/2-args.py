#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = len(sys.argv) - 1
    if argument == 0:
        print("0 arguments.")
    elif argument == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argument))
    for a in range(1, argument + 1):
        print("{}: {}".format(a, sys.argv[a]))
