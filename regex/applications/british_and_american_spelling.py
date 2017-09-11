#!/usr/bin/env python3

import re


# British and American Style of Spelling
# https://www.hackerrank.com/challenges/uk-and-us/problem
def british_english_diff_count_1(text, tests):
    for test in tests:
        pattern = r'\b{}[sz]e\b'.format(test[:-2])
        matches = re.findall(pattern, text)
        print(len(matches))


# UK and US: Part 2
# https://www.hackerrank.com/challenges/uk-and-us-2/problem
def british_english_diff_count_2(text, tests):
    seq = 'our'

    for test in tests:
        start = test.index(seq)
        end = start + len(seq)
        pattern = r'\b{}(or|our){}\b'.format(test[:start], test[end:])
        matches = re.findall(pattern, text)
        print(len(matches))


if __name__ == '__main__':
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(input())

    tests = []
    t = int(input())
    for _ in range(t):
        tests.append(input())

    british_english_diff_count_1('\n'.join(lines), tests)
    british_english_diff_count_2('\n'.join(lines), tests)
