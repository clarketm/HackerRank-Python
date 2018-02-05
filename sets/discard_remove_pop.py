#!/usr/bin/env python3

# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        method, *args = input().split()
        getattr(s, method)(*map(int, args))

    print(sum(s))
