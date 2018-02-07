#!/usr/bin/env python3

# Triangle Quest
# https://www.hackerrank.com/challenges/python-quest-1/problem


if __name__ == '__main__':
    for i in range(1, int(input())):
        # Using `string`
        # print(i * int('1' * i))

        # Using `mathematical approach w/ for loop`
        # print((sum([10 ** j for j in range(1, i)]) + 1) * i)

        # Using `mathematical approach w/out for loop`
        print((10 ** i // 9) * i)
