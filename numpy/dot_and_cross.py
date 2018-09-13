#!/usr/bin/env python3

# Dot and Cross
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

if __name__ == '__main__':
    N = int(input())
    A = numpy.array([input().split() for _ in range(N)], dtype=int)
    B = numpy.array([input().split() for _ in range(N)], dtype=int)
    print(numpy.dot(A, B))
