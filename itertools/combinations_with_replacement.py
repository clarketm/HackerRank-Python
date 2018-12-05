#!/usr/bin/env python3

# itertools.combinations_with_replacement()
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement


def get_combinations(string, max_chars):
    combos = sorted(
        map("".join, map(sorted, combinations_with_replacement(string, max_chars)))
    )
    print("\n".join(combos))


if __name__ == "__main__":
    string, max_chars = input().split()
    get_combinations(string, int(max_chars))
