#!/usr/bin/python3
str = "{}"
for n in range(97, 123):
    if n != 101 and n != 113:
        print(str.format(chr(n)), end="")
