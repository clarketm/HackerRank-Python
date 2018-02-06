#!/usr/bin/env python3

# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem


def is_strict_superset(A, n):
    for _ in range(n):
        s = {int(item) for item in input().split()}
        if not A.issuperset(s):
            return False
    return True


if __name__ == '__main__':
    A = {int(item) for item in input().split()}
    n = int(input())
    print(is_strict_superset(A, n))
