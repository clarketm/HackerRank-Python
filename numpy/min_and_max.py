#!/usr/bin/env python3

# Min and Max
# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(N)], dtype=int)
    print(numpy.max(numpy.min(arr, axis=1)))
