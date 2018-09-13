#!/usr/bin/env python3

# from operator import itemgetter

# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

# Globals
student_grade_map = []


def sort_students_by_grade_name():
    global student_grade_map

    student_grade_map = sorted(student_grade_map, key=lambda k: (k[1], k[0]))
    # student_grade_map = sorted(student_grade_map, key=itemgetter(1, 0))

    # find `second` lowest score
    find_lowest(find_lowest(), True)


def find_lowest(student_index=0, is_print=False):
    global student_grade_map

    lowest = student_grade_map[student_index][1]

    while student_grade_map[student_index][1] == lowest:
        print(student_grade_map[student_index][0]) if is_print else None
        student_index += 1

    return student_index


if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        name = input()
        grade = float(input())
        student_grade_map.append([name, grade])

    sort_students_by_grade_name()
