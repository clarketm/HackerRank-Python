#!/usr/bin/env python3

import re


# Split the Phone Numbers
# https://www.hackerrank.com/challenges/split-number/problem
def split_phone_number(phone_number):
    # [Country code]-[Local Area Code]-[Number]
    # Group 1 = [Country code]
    # Group 2 = [Local Area Code]
    # Group 3 = [Number]
    # There might either be a '-' ( ascii value 45), or a ' ' ( space, ascii value 32) between the segments
    # Where the country and local area codes can have 1-3 numerals each and the number section can have 4-10 numerals each.
    match = re.match(r'(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})', phone_number)
    print("CountryCode={},LocalAreaCode={},Number={}".format(match.group(1), match.group(2), match.group(3)))


if __name__ == '__main__':
    n = int(input())
    while n > 0:
        phone_number = input()
        split_phone_number(phone_number)
        n -= 1
