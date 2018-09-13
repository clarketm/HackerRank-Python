#!/usr/bin/env python3

# Mod Divmod
# https://www.hackerrank.com/challenges/python-mod-divmod/problem

if __name__ == '__main__':
    numerator = int(input())
    denominator = int(input())

    # quotient
    print(numerator // denominator)

    # remainder
    print(numerator % denominator)

    # quotient and remainder
    print(divmod(numerator, denominator))
