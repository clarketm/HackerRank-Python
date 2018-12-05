#!/usr/bin/env python3

# DefaultDict Tutorial
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

# The defaultdict tool is a container in the collections class of Python.
# It's similar to the usual dictionary (dict) container, but it has one difference:
# The value fields' data type is specified upon initialization.

from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())

    A = []
    B = defaultdict(list)

    for _ in range(n):
        A.append(input())

    for index, key in enumerate(A):
        B[key].append(index + 1)

    for _ in range(m):
        print(" ".join(str(index) for index in B.get(input(), [-1])))
        # try:
        #     print(' '.join(str(index) for index in B.get(input())))
        # except:
        #     print(-1)
