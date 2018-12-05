#!/usr/bin/env python3

# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == "__main__":
    M = int(input())
    s1 = set(map(int, input().split()))

    N = int(input())
    s2 = set(map(int, input().split()))

    # Using `difference`
    # diff = s1.difference(s2)
    # diff.update(s2.difference(s1))

    # Using `symmetric_difference`
    diff = s1.symmetric_difference(s2)

    print(*sorted(diff), sep="\n")
