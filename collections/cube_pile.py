#!/usr/bin/env python3

# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

# Using `<` and `ending` terminating condition
# def is_stackable(quantity, cubes):
#     prev = None
#     cur = None
#     left_ptr = 0
#     right_ptr = quantity - 1
#
#     while left_ptr < right_ptr:
#         left = cubes[left_ptr]
#         right = cubes[right_ptr]
#
#         if left >= right:
#             prev, cur = cur, left
#             left_ptr += 1
#         elif right > left:
#             prev, cur = cur, right
#             right_ptr -= 1
#
#         if (prev and cur) and (cur > prev):
#             return 'No'
#
#     return 'Yes'


# Using `<=` and `beginning` terminating condition
def is_stackable(quantity, cubes):
    prev = None
    cur = None
    left_ptr = 0
    right_ptr = quantity - 1

    while left_ptr <= right_ptr:
        left = cubes[left_ptr]
        right = cubes[right_ptr]

        if (prev and cur) and (cur > prev):
            return 'No'
        elif left >= right:
            prev, cur = cur, left
            left_ptr += 1
        elif right > left:
            prev, cur = cur, right
            right_ptr -= 1

    return 'Yes'


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        quantity = int(input())
        # cubes = list(map(int, input().split()))
        cubes = [int(cube) for cube in input().split()]
        print(is_stackable(quantity, cubes))
