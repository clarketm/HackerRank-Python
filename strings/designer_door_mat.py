#!/usr/bin/env python3

# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem


# Using a functional, `pythonic` approach
def create_mat(N, M):
    for i in range(1, N, 2):
        print((i * '.|.').center(M, '-'))

    print('WELCOME'.center(M, '-'))

    for i in range(N - 2, -1, -2):
        print((i * '.|.').center(M, '-'))


# Using an iterative, `unpythonic` approach
# def create_mat(N, M):
#     greeting = 'WELCOME'
#
#     count = 0
#     for i in range(1, N, 2):
#         for dash in range((M // 2) - (count * 3)):
#             print('-', end='')
#         for dot_line in range(i):
#             print('.|.', end='')
#         for dash in range((M // 2) - (count * 3)):
#             print('-', end='')
#         print()
#         count += 1
#
#     print('-' * (((M - len(greeting)) // 2) + 1), end='')
#     print(greeting, end='')
#     print('-' * (((M - len(greeting)) // 2) + 1), end='')
#     print()
#
#     count = N // 2 - 1
#     for i in range(N - 2, -1, -2):
#         for dash in range((M // 2) - (count * 3)):
#             print('-', end='')
#         for dot_line in range(i):
#             print('.|.', end='')
#         for dash in range((M // 2) - (count * 3)):
#             print('-', end='')
#         print()
#         count -= 1


if __name__ == '__main__':
    N, M = map(int, input().split())
    create_mat(N, M)
