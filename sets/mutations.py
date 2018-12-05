#!/usr/bin/env python3

# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == "__main__":
    A = int(input())
    s0 = {int(i) for i in input().split()}
    N = int(input())

    for _ in range(N):
        method, _ = input().split()
        s1 = {int(i) for i in input().split()}
        getattr(s0, method)(s1)

    print(sum(s0))
