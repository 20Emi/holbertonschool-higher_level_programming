#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for n in range(len(sys.argv) - 1):
        result = result + int(sys.argv[n + 1])
    print("{}".format(result))
