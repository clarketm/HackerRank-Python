#!/usr/bin/env python3

# Polar Coordinates
# https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import phase

if __name__ == "__main__":
    complex_number = complex(input())

    print(abs(complex_number))
    print(phase(complex_number))

    # print(*polar(complex_number), sep='\n')
