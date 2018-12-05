#!/usr/bin/env python3

# itertools.product()
# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

if __name__ == "__main__":
    A = map(int, input().split())
    B = map(int, input().split())

    print(*product(A, B))
