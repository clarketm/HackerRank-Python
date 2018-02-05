#!/usr/bin/env python3

# Any or All
# https://www.hackerrank.com/challenges/any-or-all/problem

if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split()))

    is_positive = all(n > 0 for n in array)

    # Using `reversed`
    # is_palindrome = any(str(n) == ''.join(reversed(str(n))) for n in array)

    # Using `slicing`
    is_palindrome = any(str(n) == str(n)[::-1] for n in array)

    print(is_positive and is_palindrome)
