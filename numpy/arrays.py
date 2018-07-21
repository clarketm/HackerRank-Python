#!/usr/bin/env python3

# Arrays
# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

if __name__ == '__main__':
    arr = input().split()
    print(numpy.array(arr[::-1], float))
