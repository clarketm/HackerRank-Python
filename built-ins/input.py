#!/usr/bin/env python3

# Input()
# https://www.hackerrank.com/challenges/input/problem

if __name__ == '__main__':
    x, k = map(int, input().split())
    expr = input()

    print(eval(expr) == k)
