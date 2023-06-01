#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    las_digit = number % 10
    print("{:d}".format(las_digit), end='')
    return las_digit
