#!/usr/bin/env python3

# Text Wrap
# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == "__main__":
    string = input()
    max_width = int(input())
    print(wrap(string, max_width))
