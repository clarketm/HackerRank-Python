#!/usr/bin/env python3

# Polynomials
# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy

if __name__ == '__main__':
    val = numpy.polyval(list(map(float, input().split())), float(input()))
    print(val)
