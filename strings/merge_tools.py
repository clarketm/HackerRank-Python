#!/usr/bin/env python3

# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem


from collections import OrderedDict
import textwrap


def merge_the_tools(s, k):
    segments = textwrap.wrap(s, k)
    print(*list(''.join(OrderedDict.fromkeys(segment)) for segment in segments), sep='\n')


if __name__ == '__main__':
    s, k = input(), int(input())
    merge_the_tools(s, k)
