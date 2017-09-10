#!/usr/bin/env python3

# Python If-Else


def if_else(n):
    # odd, print Weird
    if n % 2 == 1:
        print("Weird")
    else:
        # even and greater than 20
        if n > 20:
            print("Not Weird")
        # even and in the inclusive range of 6 to 20
        elif n > 5:
            print("Weird")
        # even and in the inclusive range of 2 to 5
        elif n > 1:
            print("Not Weird")


if __name__ == '__main__':
    n = int(input())
    if_else(n)
