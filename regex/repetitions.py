#!/usr/bin/env python3


import re


# Matching {x} Repetitions
# https://www.hackerrank.com/challenges/matching-x-repetitions/problem
def match_x_repetitions(string):
    # S must be of length equal to 45.
    # The first 40 characters should consist of letters(both lowercase and uppercase), or of even digits.
    # The last 5 characters should consist of odd digits or whitespace characters.
    match = re.match(r'^[a-zA-Z02468]{40}[13579\s]{5}$', string)
    print(str(bool(match)).lower())


# Matching {x, y} Repetitions
# https://www.hackerrank.com/challenges/matching-x-y-repetitions/problem
def match_x_y_repetitions(string):
    # S should begin with 1 or 2 digits.
    # After that, S should have 3 or more letters (both lowercase and uppercase).
    # Then S should end with up to 3 . symbol(s). You can end with 0 to 3 . symbol(s), inclusively.
    match = re.match(r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$', string)
    print(str(bool(match)).lower())


# Matching Zero Or More Repetitions
# https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions/problem
def match_zero_or_more_repetitions(string):
    # S should begin with 2 or more digits.
    # After that, S should have 0 or more lowercase letters.
    # S should end with 0 or more uppercase letters
    match = re.match(r'^\d{2,}[a-z]*[A-Z]*$', string)
    print(str(bool(match)).lower())


# Matching One Or More Repetitions
# https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem
def match_one_or_more_repetitions(string):
    # S should begin with 1 or more digits.
    # After that, S should have 1 or more uppercase letters.
    # S should end with 1 or more lowercase letters
    match = re.match(r'^\d+[A-Z]+[a-z]+$', string)
    print(str(bool(match)).lower())


# Matching Ending Items
# https://www.hackerrank.com/challenges/matching-ending-items/problem
def match_ending_items(string):
    # S should consist of only lowercase and uppercase letters (no numbers or symbols).
    # S should end in s.
    match = re.match(r'^[a-zA-Z]*s$', string)
    print(str(bool(match)).lower())


if __name__ == '__main__':
    string = input()
    # match_x_repetitions(string)
    # match_x_y_repetitions(string)
    # match_zero_or_more_repetitions(string)
    # match_one_or_more_repetitions(string)
    # match_ending_items(string)
