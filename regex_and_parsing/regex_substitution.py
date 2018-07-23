#!/usr/bin/env python3

# Regex Substitution
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

if __name__ == '__main__':
    N = int(input())
    text = "\n".join([input() for _ in range(N)])

    s = re.sub(r"(?<= )&&(?= )", "and", text)
    s = re.sub(r"(?<= )\|\|(?= )", "or", s)

    print(s)
