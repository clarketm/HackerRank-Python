#!/usr/bin/env python3

# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == "__main__":
    N = int(input())
    student_average_map = {}

    for _ in range(N):
        student, *grades = input().split()
        grades = list(map(float, grades))
        student_average_map[student] = sum(grades) / len(grades)

    print("{0:.2f}".format(student_average_map[input()], 2))
