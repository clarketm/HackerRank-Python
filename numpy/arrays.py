#!/usr/bin/env python3

# Arrays
# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)


if __name__ == '__main__':
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)
