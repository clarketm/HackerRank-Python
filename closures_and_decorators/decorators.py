#!/usr/bin/env python3

# Standardize Mobile Number Using Decorators
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

# import re


def wrapper(f):
    def fun(l):
        # using FOR LOOP w/ regex
        # for index, value in enumerate(l):
        #     match = re.match(r'(\+91|91|0)?(\d{5})(\d{5})', value)
        #     l[index] = '+91 {} {}'.format(match.group(2), match.group(3))

        # using LIST COMPREHENSION w/ regex
        # l = ['+91 {} {}'.format(m.group(2), m.group(3)) for v in l for m in [re.match(r'(\+91|91|0)?(\d{5})(\d{5})', v)] if m]

        # f(l)

        # using SLICES
        f(['+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l])

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
