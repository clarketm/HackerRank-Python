#!/usr/bin/env python3

import re


# British and American Style of Spelling
# https://www.hackerrank.com/challenges/uk-and-us/problem
def british_english_diff_count(text, tests):
    for test in tests:
        pattern = r'{}[sz]e'.format(test[:-2])
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

    british_english_diff_count('\n'.join(lines), tests)
