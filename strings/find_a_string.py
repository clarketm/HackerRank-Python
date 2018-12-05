#!/usr/bin/env python3

# Find a String
# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, substring):
    length = len(substring)
    i, count = 0, 0

    # Using `while`
    # while i < len(string):
    #     if substring == string[i:i + length]:
    #         count += 1
    #     i += 1

    # Using `while` optimized
    while i < len(string) - (length - 1):
        if substring == string[i : i + length]:
            count += 1
        i += 1

    # Using `for` w/ `enumerate`
    # for i, c in enumerate(string):
    #     if substring == string[i:i + length]:
    #         count += 1

    # Using `for` w/ `range`
    # for i in range(len(string)):
    #     if substring == string[i:i + length]:
    #         count += 1

    return count


if __name__ == "__main__":
    string = input()
    substring = input()
    print(count_substring(string, substring))
