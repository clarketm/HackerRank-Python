#!/usr/bin/env python3

import re


# Positive Lookahead
# https://www.hackerrank.com/challenges/positive-lookahead/problem
def positive_lookeahead(string):
    # Write a regex that can match all occurrences of `o` followed immediately by `oo` in S.
    matches = re.findall(r'o(?=oo)', string)
    print(len(matches))


# Negative Lookahead
# https://www.hackerrank.com/challenges/negative-lookahead/problem
def negative_lookeahead(string):
    # If S = `goooo`, then regex should match `goooo`. Because the first g is not follwed by g and the last o is not followed by o.
    matches = re.findall(r'^(.)(?!\1)', string)
    print(len(matches))


# Positive Lookbehind
# https://www.hackerrank.com/challenges/positive-lookbehind/problem
def positive_lookbehind(string):
    # Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
    matches = re.findall(r'(?<=[13579])\d', string)
    print(len(matches))


# Negative Lookbehind
# https://www.hackerrank.com/challenges/negative-lookbehind/problem
def negative_lookbehind(string):
    # Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).
    matches = re.findall(r'(?<![aeiouAEIOU]).', string)
    print(len(matches))


if __name__ == '__main__':
    string = input()
    # positive_lookeahead(string)
    # negative_lookeahead(string)
    # positive_lookbehind(string)
    # negative_lookbehind(string)
