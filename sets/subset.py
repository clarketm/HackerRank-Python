#!/usr/bin/env python3

# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    for i in range(int(input())):
        a = int(input())
        A = set(input().split())
        b = int(input())
        B = set(input().split())
        print(A.issubset(B))
