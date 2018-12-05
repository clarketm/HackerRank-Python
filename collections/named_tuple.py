#!/usr/bin/env python3

# Collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    Student = namedtuple("Student", input().split())

    # LIST COMPREHENSIONS
    average = sum([int(Student(*input().split()).MARKS) for student in range(n)]) / n
    print("{:.2f}".format(average))

    # FOR LOOP
    # total = 0
    # for _ in range(n):
    #     student = Student(*input().split())
    #     total += int(student.MARKS)
    #
    # print("{:.2f}".format(total / n))
