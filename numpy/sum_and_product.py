#!/usr/bin/env python3

# Sum and Product
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

if __name__ == '__main__':
    N, M = map(int, input().split())
    # arr = numpy.array([list(map(int, input().split())) for _ in range(N)])
    arr = numpy.array([input().split() for _ in range(N)], dtype=int)
    print(numpy.prod(numpy.sum(arr, axis=0), axis=0))
