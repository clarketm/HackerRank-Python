#!/usr/bin/env python3

import re


# Saying Hi
# https://www.hackerrank.com/challenges/saying-hi/problem
def say_hi(string):
    # The first character must be the letter H or h
    # The second character must be the letter I or i
    # The third character must be a single space (i.e. \s)
    # The fourth character must NOT be the letter D or d
    match = re.match(r'^[Hh][Ii]\s[^Dd]', string)
    if bool(match):
        print(string)


if __name__ == '__main__':
    n = int(input())
    while n > 0:
        string = input()
        say_hi(string)
        n -= 1
