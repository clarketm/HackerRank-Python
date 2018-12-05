#!/usr/bin/env python3

# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == "__main__":
    n, m = map(int, input().split())

    array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    # Using an `iterative` approach
    # happiness = 0
    # for i in A:
    #     if i in array:
    #         happiness += 1
    #
    # for i in B:
    #     if i in array:
    #         happiness -= 1
    #
    # print(happiness)

    # Using an `list comprehension` approach
    pos_list = [int(i in A) - int(i in B) for i in array]
    print(sum(pos_list))
