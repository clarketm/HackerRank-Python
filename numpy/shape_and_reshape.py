#!/usr/bin/env python3

# Shape and Reshape
# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    result = numpy.array(arr)
    result.shape = (3, 3)
    print(result)
