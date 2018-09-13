#!/usr/bin/env python3

import re
import sys


# Building a Smart IDE: Programming Language Detection
# https://www.hackerrank.com/challenges/programming-language-detection/problem
def detect_language(snippet):
    if is_c(snippet):
        print('C')
    elif is_java(snippet):
        print('Java')
    elif is_python(snippet):
        print('Python')


def is_c(snippet):
    # TODO: add more conditions
    return bool(re.search(r'#include', snippet))


def is_java(snippet):
    # TODO: add more conditions
    return bool(re.search(r'import java', snippet))


def is_python(snippet):
    # TODO: add more conditions
    return bool(re.search(r'(def|print )', snippet))


if __name__ == '__main__':
    snippet = sys.stdin.read()
    detect_language(snippet)
