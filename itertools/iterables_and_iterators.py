#!/usr/bin.env python3

# Iterables and Iterators
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    letters = input().split()
    K = int(input())

    combs = list(combinations(letters, K))

    # Using `filter`
    with_a = list(filter(lambda i: "a" in i, combs))

    # Using `list comprehension`
    # with_a = [i for i in combs if 'a' in i]

    print("{:.3f}".format(len(with_a) / len(combs)))
