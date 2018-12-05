#!/usr/bin/env python3

# Print Function


def print_range(n):
    # print [1, n]
    for i in range(1, n + 1):
        print(i, end="")


if __name__ == "__main__":
    n = int(input())
    print_range(n)
