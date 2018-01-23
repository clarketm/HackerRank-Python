#!/usr/bin/env python3

# Collections.deque()
# https://www.hackerrank.com/challenges/py-collections-deque/problem


from collections import deque

if __name__ == '__main__':
    N = int(input())

    q = deque()

    for _ in range(N):
        # Using `var args` to circumvent exception
        method, *args = input().split()
        getattr(q, method)(*args)

        # Using `try/except` to circumvent exception
        # operation = input()
        # try:
        #     method, arg = operation.split()
        #     getattr(q, method)(int(arg))
        # except ValueError:
        #     method = operation
        #     getattr(q, method)()

    print(*q)
