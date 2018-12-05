#!/usr/bin/env python3

# Re.start() & Re.end()
# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

if __name__ == "__main__":
    S = input()
    k = input()

    p = re.compile(k)
    m = p.search(S)

    if not m:
        print((-1, -1))

    while m:
        start = m.start()
        end = m.end() - 1
        print((start, end))
        m = p.search(S, start + 1)
