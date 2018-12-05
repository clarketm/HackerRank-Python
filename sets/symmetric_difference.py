#!/usr/bin/env python3

# Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == "__main__":
    n = int(input())
    # english = set(map(int, input().split()))
    english = {int(i) for i in input().split()}
    b = int(input())
    # french = set(map(int, input().split()))
    french = {int(i) for i in input().split()}

    # Using `^`
    print(len(english ^ french))

    # Using 'symmetric_difference'
    # Note: symmetric_difference is commutative
    # subscribed_english_or_french = english.symmetric_difference(french)
    # subscribed_english_or_french = french.symmetric_difference(english)
    # print(len(subscribed_english_or_french))
