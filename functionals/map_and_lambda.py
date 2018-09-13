#!/usr/bin/env python3

# Map and Lambda Function
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


def cube(x): return x ** 3


def fibonacci(n):
    seq = [0, 1]

    for i in range(2, n):
        seq.append(seq[i - 2] + seq[i - 1])

    return [cube(i) for i in seq]


# def fibonacci(n):
#     seq = []

#     for i in range(n):
#         if i <= 1:
#             seq.append(i)
#         else:
#             seq.append(seq[i - 2] + seq[i - 1])

#     return list(map(cube, seq))


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
