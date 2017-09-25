#!/usr/bin/env python3

# Group(), Groups() & Groupdict()
# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

if __name__ == '__main__':
    string = input()
    match = re.search(r'([a-zA-Z0-9])\1', string)
    print(match.group(1) if match else -1)
