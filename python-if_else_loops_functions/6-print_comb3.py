#!/usr/bin/python3

for num in range(0, 10):
    for num1 in range((1+num), 10):
        if num == 0 and num1 == 1:
            print("{}{}".format(num, num1), end='')
        elif num1 != num:
            print(", {}{}".format(num, num1), end='')
print()
