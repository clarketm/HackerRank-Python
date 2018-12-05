#!/usr/bin/env python3

# Transpose and Flatten
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(N)], dtype=int)
    print(numpy.transpose(arr))
    print(arr.flatten())
