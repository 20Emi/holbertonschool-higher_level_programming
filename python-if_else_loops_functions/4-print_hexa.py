#!/usr/bin/python3
str = "{}"
for n in range(0, 99):
    print(n, '=', str.format(hex(n)))
