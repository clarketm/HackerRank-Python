#!/usr/bin/env python3

# What's Your Name?
# https://www.hackerrank.com/challenges/whats-your-name/problem


def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == "__main__":
    first = input()
    last = input()
    print_full_name(first, last)
