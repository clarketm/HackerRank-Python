#!/usr/bin/env python3

# sWAP cASE
# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    # Using swapcase
    # return ''.join(map(str.swapcase, s))

    # Using list comprehension
    # return ''.join([c.lower() if c.isupper() else c.upper() if c.islower() else c for c in s])

    # Using iterative approach
    new_s = []

    for c in s:
        if c.islower():
            new_s.append(c.upper())
        elif c.isupper():
            new_s.append(c.lower())
        else:
            new_s.append(c)

    return ''.join(new_s)


if __name__ == '__main__':
    print(swap_case(input()))
