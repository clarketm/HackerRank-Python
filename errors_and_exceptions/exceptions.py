#!/usr/bin/env python3

# Exceptions
# https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        try:
            numerator, denominator = map(int, input().split())
            print(numerator // denominator)
        except (ValueError, ZeroDivisionError) as e:
            print('Error Code:', e)
