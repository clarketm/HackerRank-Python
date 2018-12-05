#!/usr/bin/env python3

# Power - Mod Power
# https://www.hackerrank.com/challenges/python-power-mod-power/problem

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())

    # a^b
    # print(a ** b)
    print(pow(a, b))

    # a^b mod m
    # print(a ** b % m)
    print(pow(a, b, m))
