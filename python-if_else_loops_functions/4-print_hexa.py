#!/usr/bin/python3
str = "{}"
for n in range(0, 98):
    print(n, '=', str.format(hex(n)))