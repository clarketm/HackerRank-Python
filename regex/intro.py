#!/usr/bin/env python3

import re


# Matching Specific String
# https://www.hackerrank.com/challenges/matching-specific-string/problem
def match_specific_string(string):
    pattern = r"hackerrank"
    match = re.findall(pattern, string)
    print("Number of matches :", len(match))


# Matching Anything But a Newline
# https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem
def match_anything_but_newline(string):
    pattern = r"^(.{3}\.){3}.{3}$"
    match = re.match(pattern, string)
    print(str(bool(match)).lower())


# Matching Digits & Non-Digit Characters
# https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem
def match_digits_and_nondigits(string):
    pattern = r"(\d{2}\D){2}\d{4}"
    match = re.search(pattern, string)
    print(str(bool(match)).lower())


# Matching Whitespace & Non-Whitespace Character
# https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem
def match_whitespace_and_nonwhitespace(string):
    pattern = r"(\S{2}\s){2}\S{2}"
    match = re.search(pattern, string)
    print(str(bool(match)).lower())


# Matching Word & Non-Word Character
# https://www.hackerrank.com/challenges/matching-word-non-word/problem
def match_word_and_nonword(string):
    pattern = r"\w{3}\W\w{10}\W\w{3}"
    match = re.search(pattern, string)
    print(str(bool(match)).lower())


# Matching Start & End
# https://www.hackerrank.com/challenges/matching-start-end/problem
def match_start_and_end(string):
    pattern = r"^\d\w{4}\.$"
    match = re.search(pattern, string)
    print(str(bool(match)).lower())


if __name__ == "__main__":
    string = input()
    # match_specific_string(string)
    # match_anything_but_newline(string)
    # match_digits_and_nondigits(string)
    # match_whitespace_and_nonwhitespace(string)
    # match_word_and_nonword(string)
    # match_start_and_end(string)
