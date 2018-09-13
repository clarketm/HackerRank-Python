#!/usr/bin/env python3

import re


# Find HackerRank
# https://www.hackerrank.com/challenges/find-hackerrank/problem
def hackerrank_count(string):
    # Print 0 if the conversation starts and ends with hackerrank
    # Print 1 if the conversation starts with hackerrank
    # Print 2 if the conversation ends with hackerrank
    # Print -1 if none of the above.
    if bool(re.search(r'^hackerrank$', string)):
        print(0)
    elif bool(re.search(r'^hackerrank', string)):
        print(1)
    elif bool(re.search(r'hackerrank$', string)):
        print(2)
    else:
        print(-1)


if __name__ == '__main__':
    n = int(input())
    while n > 0:
        string = input()
        hackerrank_count(string)
        n -= 1
