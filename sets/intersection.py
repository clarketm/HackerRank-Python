#!/usr/bin/env python3

# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


if __name__ == '__main__':
    n = int(input())
    # english = set(map(int, input().split()))
    english = {int(i) for i in input().split()}
    b = int(input())
    # french = set(map(int, input().split()))
    french = {int(i) for i in input().split()}

    # Using `&`
    print(len(english & french))

    # Using 'intersection'
    # Note: union is commutative
    # subscribed = english.intersection(french)
    # subscribed =  french.intersection(english)
    # print(len(subscribed))
