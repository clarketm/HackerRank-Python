#!/usr/bin/env python3

# Linear Algebra
# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy

if __name__ == '__main__':
    N = int(input())
    arr = numpy.array([input().split() for _ in range(N)], dtype=float)
    numpy.set_printoptions(legacy='1.13')
    print(numpy.linalg.det(arr))
