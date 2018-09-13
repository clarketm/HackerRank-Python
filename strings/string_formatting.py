#!/usr/bin/env python3

# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    width = len(format(number, 'b'))

    for n in range(1, number + 1):
        # Using formatted string literals
        # print(f'{n:{width}d} {n:{width}o} {n:{width}X} {n:{width}b}')

        # Using the string `format` method
        print('{number:{width}d} {number:{width}o} {number:{width}X} {number:{width}b}'.format(number=n, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
