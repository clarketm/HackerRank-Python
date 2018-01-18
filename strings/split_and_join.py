#!/usr/bin/env python3

# String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    # Using `print`
    # return print(*line.split(), sep='-')

    # Using `replace`
    # return line.replace(' ', '-')

    # Using `split` and `join`
    return '-'.join(line.split(' '))


if __name__ == '__main__':
    line = input()
    print(split_and_join(line))
