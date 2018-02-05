#!/usr/bin/env python3

# ginortS
# https://www.hackerrank.com/challenges/ginorts/problem

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# `lower priority` => `higher priority`

if __name__ == '__main__':
    S = input()
    S = 'Sorting1234'
    S_sorted = sorted(S, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x))

    print(''.join(S_sorted))

    # One-liner
    # print(*sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)), sep='')
