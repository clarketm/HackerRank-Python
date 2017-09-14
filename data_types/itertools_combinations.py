#!/usr/bin/env python3


# itertools.combinations()
# https://www.hackerrank.com/challenges/itertools-combinations/problem


from itertools import combinations


def get_combinations(string, max_chars):
    # USING LIST COMPREHENSIONS
    # result = [sorted(map(''.join, map(sorted, combinations(string, i)))) for i in range(1, max_chars + 1)]
    # print('\n'.join(str(row) for vector in result for row in vector))

    for i in range(1, max_chars + 1):
        combos = sorted(map(''.join, map(sorted, combinations(string, i))))
        print('\n'.join(combos))


if __name__ == '__main__':
    string, max_chars = input().split()
    get_combinations(string, int(max_chars))
