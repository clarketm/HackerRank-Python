#!/usr/bin/env python3

import re


# Valid PAN format
# https://www.hackerrank.com/challenges/valid-pan-format/problem
def validate(id):
    # <char><char><char><char><char><digit><digit><digit><digit><char>
    # Each char is an uppercase letter
    # Each digit lies between 0 and 9
    # The length of the PAN number is always 10
    match = re.match(r'^[A-Z]{5}\d{4}[A-Z]$', id)
    result = 'YES' if bool(match) else 'NO'
    print(result)


if __name__ == '__main__':
    n = int(input())
    while n > 0:
        id = input()
        validate(id)
        n -= 1
