#!/usr/bin/env python3

# Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    # Using list
    # s_list = list(string)
    # s_list[position] = character
    # return ''.join(s_list)

    # Using slices
    return string[:position] + c + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
