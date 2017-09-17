#!/usr/bin/env python3

# Introduction to Regex Module
# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        match = re.match(r'^[+\-.]?\d*\.\d+$', input())
        print(bool(match))
