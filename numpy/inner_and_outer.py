#!/usr/bin/env python3

# Inner and Outer
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy

if __name__ == "__main__":
    A = numpy.array(input().split(), dtype=int)
    B = numpy.array(input().split(), dtype=int)
    print(numpy.inner(A, B))
    print(numpy.outer(A, B))
