#!/usr/bin/env python3


import re


# Matching Specific Characters
# https://www.hackerrank.com/challenges/matching-specific-characters/problem
def match_specific_characters(string):
    # S must be of length: 6
    # First character: 1, 2 or 3
    # Second character: 1, 2 or 0
    # Third character: x, s or 0
    # Fourth character: 3, 0 , A or a
    # Fifth character: x, s or u
    # Sixth character: . or ,
    match = re.match(r'^[123][012][0sx][03Aa][sux][.,]$', string)
    print(str(bool(match)).lower())


# Excluding Specific Characters
# https://www.hackerrank.com/challenges/excluding-specific-characters/problem
def exclude_specific_characters(string):
    # S must be of length 6.
    # First character should NOT be a digit (0-9).
    # Second character should NOT be a lowercase vowel (aeiou).
    # Third character should NOT be b, c, D or F.
    # Fourth character should NOT be a whitespace character ( \r, \n, \t, \f or <space> ).
    # Fifth character should NOT be a uppercase vowel (AEIOU).
    # Sixth character should NOT be a . or , symbol.
    match = re.match(r'^[\D][^aeiou][^bcDF][\S][^AEIOU][^.,]$', string)
    print(str(bool(match)).lower())


# Matching Character Ranges
# https://www.hackerrank.com/challenges/matching-range-of-characters/problem
def match_character_ranges(string):
    # The string's length is >= 5.
    # The first character must be a lowercase English alphabetic character.
    # The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
    # The third character must NOT be a lowercase English alphabetic character.
    # The fourth character must NOT be an uppercase English alphabetic character.
    # The fifth character must be an uppercase English alphabetic character.
    match = re.match(r'^[a-z][1-9][^a-z][^A-Z][A-Z].*$', string)
    print(str(bool(match)).lower())


if __name__ == '__main__':
    string = input()
    # match_specific_characters(string)
    # exclude_specific_characters(string)
    # match_character_ranges(string)
