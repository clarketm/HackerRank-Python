#!/usr/bin/env python3

# Concatenate
# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

if __name__ == '__main__':
    N, M, P = map(int, input().split())

    # Solution 1: Loop
    # arr = []

    # for i in range(N + M):
    #     arr.append(list(map(int, input().split())))

    # print(arr)

    # Solution 2: List Comprehension
    # arr = [list(map(int, input().split())) for _ in range(N + M)]
    # print(arr)

    # Solution 3: Numpy
    arrN = numpy.array([input().split() for _ in range(N)], int)
    arrM = numpy.array([input().split() for _ in range(M)], int)

    arr = numpy.concatenate((arrN, arrM))
    print(arr)
