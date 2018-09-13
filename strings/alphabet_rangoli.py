#!/usr/bin/env python3

# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# Using a `terse` approach
# def print_rangoli(size):
#     import string
#     alpha = string.ascii_lowercase
#     l = []
#     for i in range(size):
#         s = "-".join(alpha[i:size])
#         l.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
#
#     print('\n'.join(l[::-1] + l[1:]))


# Using a `verbose` approach
def print_rangoli(size):
    start = ord('a')
    end = start + (size - 1)

    # width = ((size * 2) - 1) + ((size - 1) * 2)
    # ...simplified
    width = size * 4 - 3

    for i in range(size):
        chars = [chr(c) for c in range(end, start - 1, -1)]
        l = chars[:i] + [chars[i]] + list(reversed(chars[:i]))
        print('-'.join(l).center(width, '-'))

    for i in reversed(range(size - 1)):
        chars = [chr(c) for c in range(end, start - 1, -1)]
        l = chars[:i] + [chars[i]] + list(reversed(chars[:i]))
        print('-'.join(l).center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
