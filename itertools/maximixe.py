#!/usr/bin/env python3

# Maximize It!
# https://www.hackerrank.com/challenges/maximize-it/problem

from functools import reduce
from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())
    L = []

    for _ in range(K):
        N, *items = map(int, input().split())
        L.append(items)

    # Using `reduce`
    S = max(reduce(lambda x, y: x + y**2, l, 0) % M for l in product(*L))

    # Using `map` and `sum`
    # S = max(map(lambda x: sum(i ** 2 for i in x) % M, product(*L)))

    print(S)
