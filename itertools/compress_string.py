#!/usr/bin/env python3


# Compress the String
# https://www.hackerrank.com/challenges/compress-the-string/problem

def get_char_count(string):
    index = 0
    while index < len(string):
        char = string[index]
        count = 0
        while index < len(string) and string[index] == char:
            index += 1
            count += 1
        print("({}, {})".format(count, char), end=' ')


if __name__ == '__main__':
    string = input()
    get_char_count(string)
