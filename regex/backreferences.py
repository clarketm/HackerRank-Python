#!/usr/bin/env python3

import re


# Matching Same Text Again & Again
# https://www.hackerrank.com/challenges/matching-same-text-again-again/problem
def match_same_text_repeatedly(string):
    # S must be of length: 20
    # 1st character: lowercase letter.
    # 2nd character: word character.
    # 3rd character: whitespace character.
    # 4th character: non word character.
    # 5th character: digit.
    # 6th character: non digit.
    # 7th character: uppercase letter.
    # 8th character: letter (either lowercase or uppercase).
    # 9th character: vowel (a, e, i , o , u, A, E, I, O or U).
    # 10th character: non whitespace character.
    # 11th character: should be same as 1st character.
    # 12th character: should be same as 2nd character.
    # 13th character: should be same as 3rd character.
    # 14th character: should be same as 4th character.
    # 15th character: should be same as 5th character.
    # 16th character: should be same as 6th character.
    # 17th character: should be same as 7th character.
    # 18th character: should be same as 8th character.
    # 19th character: should be same as 9th character.
    # 20th character: should be same as 10th character.
    match = re.match(
        r"^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$",
        string,
    )
    print(str(bool(match)).lower())


# Backreferences To Failed Groups
# https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem
def backreferences_to_failed_groups(string):
    # S consists of 8 digits.
    # S may have `-` separator such that string S gets divided in 4 parts, with each part having exactly 2 digits. (Eg. 12-34-56-78)
    match = re.match(r"^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$", string)
    print(str(bool(match)).lower())


# Branch Reset Groups
# https://www.hackerrank.com/challenges/branch-reset-groups/problem
def branch_reset_groups(string):
    # S consists of 8 digits.
    # S must have "---", "-", "." or ":" separator such that string S gets divided in 4parts, with each part having exactly 2 digits.
    # S string must have exactly one kind of separator.
    # Separators must have integers on both sides.
    match = re.match(r"^\d{2}((?:---)|(?:-)|(?:.)|(?::))\d{2}\1\d{2}\1\d{2}$", string)
    print(str(bool(match)).lower())


# Forward References
# https://www.hackerrank.com/challenges/forward-references/problem
def forward_references(string):
    # S consists of `tic` or `tac`.
    # `tic` should not be immediate neighbour of itself.
    # The first `tic` must occur only when `tac` has appeared at least twice(2) before.
    match = re.match(r"^tac(tactic|tac)+$", string)
    print(str(bool(match)).lower())


if __name__ == "__main__":
    string = input()
    # match_same_text_repeatedly(string)
    # backreferences_to_failed_groups(string)
    # branch_reset_groups(string)
    # forward_references(string)
