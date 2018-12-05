#!/usr/bin/env python3

# Mean, Var and Std
# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(N)], dtype=int)
    numpy.set_printoptions(legacy="1.13")
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(numpy.std(arr, axis=None))
