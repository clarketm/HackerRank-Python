#!/usr/bin/env python3

# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem


if __name__ == '__main__':
    n = int(input())
    # english = set(map(int, input().split()))
    english = {int(i) for i in input().split()}
    b = int(input())
    # french = set(map(int, input().split()))
    french = {int(i) for i in input().split()}

    # Using `|`
    print(len(english | french))

    # Using 'union'
    # Note: union is commutative
    # subscribed = english.union(french)
    # subscribed =  french.union(english)
    # print(len(subscribed))
