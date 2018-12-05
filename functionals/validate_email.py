#!/usr/bin/env python3

# Validating Email Addresses With a Filter
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re


def fun(s):
    # It must have the username@websitename.extension format type.
    # The username can only contain letters, digits, dashes and underscores.
    # The website name can only have letters and digits.
    # The maximum length of the extension is 3.
    try:
        return bool(re.match(r"^([\w-]+)@([a-zA-Z\d]+)\.(.{,3})$", s).groups())
    except:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
