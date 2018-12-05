#!/usr/bin/env python3

# Re.split()
# https://www.hackerrank.com/challenges/re-split/problem

import re

if __name__ == "__main__":
    num = input()
    segments = filter(None, re.split(r"[.,]", num))
    print(*segments, sep="\n")
