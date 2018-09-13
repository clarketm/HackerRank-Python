#!/usr/bin/env python3

# Find Angle MBC
# https://www.hackerrank.com/challenges/find-angle/problem

from math import degrees, acos, sqrt


def calculate_angle(opp, adj1, adj2):
    return degrees(acos((adj1**2 + adj2**2 - opp**2) / (2 * adj1 * adj2)))


if __name__ == '__main__':
    c = int(input())
    a = int(input())

    b = sqrt(a**2 + c**2)
    m = b / 2

    MBC = round(calculate_angle(m, m, a))
    # MBA = round(calculate_angle(m, m, c))

    # assert MBC + MBA == 90

    # print(f'{MBC}°')
    # print(f'{MBA}°')

    print('{}°'.format(MBC))
