#!/usr/bin.env python3

# String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

# In the first line, print True if `s` has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if `s` has any alphabetical characters. Otherwise, print False.
# In the third line, print True if `s` has any digits. Otherwise, print False.
# In the fourth line, print True if `s` has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if `s` has any uppercase characters. Otherwise, print False.


def validate_string(s: str) -> None:
    # Using `for` (iterative)
    # isalnum = isalpha = isdigit = islower = isupper = False
    # for c in s:

    # -> Using single-line
    # isalnum = isalnum or c.isalnum()
    # isalpha = isalpha or c.isalpha()
    # isdigit = isdigit or c.isdigit()
    # islower = islower or c.islower()
    # isupper = isupper or c.isupper()

    # -> Using multi-line
    # if c.isalnum():
    #     isalnum = True
    # if c.isalpha():
    #     isalpha = True
    # if c.isdigit():
    #     isdigit = True
    # if c.islower():
    #     islower = True
    # if c.isupper():
    #     isupper = True

    # print(isalnum)
    # print(isalpha)
    # print(isdigit)
    # print(islower)
    # print(isupper)

    # Using `any` (functional)
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


if __name__ == '__main__':
    s = input()
    validate_string(s)
