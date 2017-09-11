#!/usr/bin/env python3


import re


# Utopian Identification Number
# https://www.hackerrank.com/challenges/utopian-identification-number/problem
def validate(id):
    # The string must begin with between 0-3 (inclusive) lowercase letters.
    # Immediately following the letters, there must be a sequence of digits (0-9). The length of this segment must be between 2 and 8, both inclusive.
    # Immediately following the numbers, there must be at least 3 uppercase letters.
    match = re.match(r'^[a-z]{,3}[0-9]{2,8}[A-Z]{3,}', id)
    result = 'VALID' if bool(match) else 'INVALID'
    print(result)


if __name__ == '__main__':
    n = int(input())
    while n > 0:
        id = input()
        validate(id)
        n -= 1
