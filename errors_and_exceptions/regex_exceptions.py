#!/usr/bin/env python3

# Incorrect Regex
# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        try:
            pattern = input()
            re.compile(pattern)
            print(True)
        except:
            print(False)
