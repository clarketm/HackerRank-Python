#!/usr/bin/env python3

import re
import sys


# Build a Stack Exchange Scraper
# https://www.hackerrank.com/challenges/stack-exchange-scraper/problem
def stack_exchange_scraper(html):
    pattern = r'"question-summary-(\d+)".*?"question-hyperlink">(.*?)<.*?"relativetime">(.*?)<'
    matches = re.findall(pattern, html, re.DOTALL)
    for match in matches:
        print(";".join(match))


if __name__ == "__main__":
    html = sys.stdin.read()
    stack_exchange_scraper(html)
