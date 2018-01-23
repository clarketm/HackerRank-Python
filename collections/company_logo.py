#!/usr/bin/env python3

# Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == "__main__":
    s = input().strip()
    letter_counts = sorted(Counter(s).items(), key=lambda item: (-item[1], item[0]))

    for letter, count in letter_counts[:3]:
        print(letter, count)
