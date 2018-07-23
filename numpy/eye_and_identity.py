#!/usr/bin/env python3

# Eye and Identity
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    numpy.set_printoptions(sign=" ")
    result = numpy.eye(N, M)
    print(result)
