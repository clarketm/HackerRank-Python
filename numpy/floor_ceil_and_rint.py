#!/usr/bin/env python3

# Floor, Ceil and Rint
# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy

if __name__ == '__main__':
    arr = numpy.array(list(map(float, input().split())))
    numpy.set_printoptions(sign=" ")
    print(numpy.floor(arr))
    print(numpy.ceil(arr))
    print(numpy.rint(arr))
