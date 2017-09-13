#!/usr/bin/env python3


# Find the Second Largest Number
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def find_second_max(array):
    array.sort()
    second_max = -2

    while array[second_max] == array[-1]:
        second_max -= 1

    return array[second_max]


if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())
    second_max = find_second_max(list(array))
    print(second_max)
