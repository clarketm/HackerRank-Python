#!/usr/bin/env python3

# Decorators 2 - Name Directory
# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem


def person_lister(f):
    def inner(people):
        # firstname(0), lastname(1), age(2), gender(3)
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
