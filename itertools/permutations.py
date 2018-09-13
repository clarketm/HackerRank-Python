#!/usr/bin/env python3

# itertools.permutations()
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()

    print(*sorted([''.join(p) for p in permutations(S, int(k))]), sep='\n')
