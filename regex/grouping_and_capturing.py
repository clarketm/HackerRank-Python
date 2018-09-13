#!/usr/bin/env python3

import re


# Matching Word Boundaries
# https://www.hackerrank.com/challenges/matching-word-boundaries/problem
def match_word_boundaries(string):
    # You have a test String S.
    # Your task is to write a regex which will match word starting with vowel (a, e, i, o, u, A, E, I , O or U).
    # The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only.
    # The matched word must start and end with a word boundary.
    match = re.match(r'\b[aeiouAEIOU][a-zA-Z]*\b', string)
    print(str(bool(match)).lower())


# Capturing & Non-Capturing Groups
# https://www.hackerrank.com/challenges/capturing-non-capturing-groups/problem
def capturing_and_nocapturing_groups(string):
    # S should have 3 or more consecutive repetitions of `ok`.
    match = re.match(r'(?:ok){3,}', string)
    print(str(bool(match)).lower())


# Alternative Matching
# https://www.hackerrank.com/challenges/alternative-matching/problem
def alternative_matching(string):
    # S must start with Mr., Mrs., Ms., Dr. or Er..
    # The rest of the string must contain one or more English alphabetic letters (upper and lowercase).
    match = re.match(r'^(?:Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$', string)
    print(str(bool(match)).lower())


if __name__ == '__main__':
    string = input()
    # match_word_boundaries(string)
    # capturing_and_nocapturing_groups(string)
    # alternative_matching(string)
