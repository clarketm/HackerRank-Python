#!/usr/bin/env python3

# Array Mathematics
# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy

if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    a = numpy.array([input().split() for _ in range(N)], dtype=int)
    b = numpy.array([input().split() for _ in range(N)], dtype=int)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a**b)
