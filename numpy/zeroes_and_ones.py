#!/usr/bin/env python3

# Zeroes and Ones
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

if __name__ == "__main__":
    dims = list(map(int, input().split()))
    zeroes = numpy.zeros(dims, dtype=numpy.int)
    ones = numpy.ones(dims, dtype=numpy.int)
    print(zeroes, ones, sep="\n")
