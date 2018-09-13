#!/usr/bin/env python3

# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Using `iterative` approach
# def is_strict_superset(A, n):
#     for _ in range(n):
#         s = {int(item) for item in input().split()}
#         if not A.issuperset(s):
#             return False
#     return True


# Using `functional` approach
def is_strict_superset(A, n):
    return all([True if A.issuperset({int(item) for item in input().split()}) else False for _ in range(n)])


if __name__ == '__main__':
    A = {int(item) for item in input().split()}
    n = int(input())
    print(is_strict_superset(A, n))
