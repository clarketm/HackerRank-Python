#!/usr/bin/env python3

# Zeroes and Ones
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    numpy.set_printoptions(sign=" ")
    result = numpy.eye(N, M)
    print(result)
