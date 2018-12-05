#!/usr/bin/env python3

# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(heights):
    heights = set(heights)
    return sum(heights) / len(heights)


if __name__ == "__main__":
    N = int(input())
    heights = list(map(int, input().split()))
    print(average(heights))
