#!/usr/bin/env python3

# Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem


if __name__ == '__main__':
    n = int(input())
    # english = set(map(int, input().split()))
    english = {int(i) for i in input().split()}
    b = int(input())
    # french = set(map(int, input().split()))
    french = {int(i) for i in input().split()}

    # Using `-`
    print(len(english - french))

    # Using 'difference'
    # Note: union is NOT commutative
    # subscribed_english_only = english.difference(french)
    # print(len(subscribed_english_only))
