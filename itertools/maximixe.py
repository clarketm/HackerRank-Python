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

    # Using `list comprehension`
    # maximums = [max(item) for item in L]

    # Using `product`
    maximums = max(product(*L))

    S = reduce(lambda x, y: x + y ** 2, maximums) % M
    print(S)
