#!/usr/bin/env python3

# Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem


def main(ints):
    _hash = hash(tuple(ints))
    print(_hash)


if __name__ == "__main__":
    n = int(input())
    ints = map(int, input().split())
    main(ints)
