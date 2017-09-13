#!/usr/bin/env python3


# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

# from operator import itemgetter

def sort_students_by_grade_name(student_grade_map):
    sorted(student_grade_map, key=lambda k: (k[1], k[0]))
    # sorted(student_grade_map, key=itemgetter(1, 0))
    print(student_grade_map)


if __name__ == '__main__':
    N = int(input())
    student_grade_map = []

    for _ in range(N):
        name = input()
        grade = float(input())
        student_grade_map.append([name, grade])
