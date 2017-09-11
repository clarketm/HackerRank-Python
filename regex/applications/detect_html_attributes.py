#!/usr/bin/env python3

import re


# Detect HTML Attributes
# https://www.hackerrank.com/challenges/html-attributes/problem
def detect_html_attributes(fragments):
    tags = {}

    for fragment in fragments:
        matches_tags = re.findall(r'<(\w+)(.*?)>', fragment)
        for match in matches_tags:
            tag = match[0]
            attrs = match[1]
            if attrs:
                attrs = re.findall(r'(\w+)(?:=["\'].*?["\'])?', attrs)
            tags.setdefault(tag, []).extend(attrs)

    for tag in sorted(tags.keys()):
        print("{}:{}".format(tag, ','.join(sorted(set(tags[tag])))))


if __name__ == '__main__':
    n = int(input())
    fragments = []
    while n > 0:
        fragment = input()
        fragments.append(fragment)
        n -= 1

    detect_html_attributes(fragments)
