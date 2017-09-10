#!/usr/bin/env python3

# Write a function


def is_leap(year):
    # The year can be evenly divided by 4, is a leap year, unless:
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
    # The year is also evenly divisible by 400. Then it is a leap year.
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return leap


if __name__ == '__main__':
    year = int(input())
    print("{}".format(is_leap(year)))
