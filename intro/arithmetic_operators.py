#!/usr/bin/env python3

# Arithmetic Operators


def sum(a, b):
    return a + b


def diff(a, b):
    return a - b


def prod(a, b):
    return a * b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print("{}".format(sum(a, b)))
    print("{}".format(diff(a, b)))
    print("{}".format(prod(a, b)))
