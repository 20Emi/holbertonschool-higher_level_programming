#!/usr/bin/python3
def uppercase(str):
    a = 0
    txt = "{}"
    for pos in range(0, len(str)):
        a = ord(str[pos])
        if a >= 97 and a <= 122:
            a = a - 32
        a = chr(a)
        print(txt.format(a), end='')
    print()
