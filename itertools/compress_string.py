#!/usr/bin/env python3

# Compress the String
# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby


def get_char_count(string):
    index = 0
    while index < len(string):
        char = string[index]
        count = 0
        while index < len(string) and string[index] == char:
            index += 1
            count += 1
        print("({}, {})".format(count, char), end=" ")


def get_char_count_using_groupby(string):
    for char, group in groupby(string):
        print("({}, {})".format(len(list(group)), char), end=" ")

    # USING LIST COMPREHENSION
    # print(*[(len(list(group)), int(char)) for char, group in groupby(string)])


if __name__ == "__main__":
    string = input()
    get_char_count(string)
    # get_char_count_using_groupby(string)
