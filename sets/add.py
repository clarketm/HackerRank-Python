#!/usr/bin/env python3

# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == "__main__":
    N = int(input())

    # Using `set comprehension`
    countries = {input() for item in range(N)}

    # Using `iterative w/ .add()`
    # countries = set()
    # for _ in range(N):
    #     countries.add(input())

    print(len(countries))
