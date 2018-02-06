#!/usr/bin/env python3

# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem


if __name__ == '__main__':
    K = int(input())
    room_list = [int(item) for item in input().split()]
    room_set = set(room_list)

    # Using a `mathematical` approach
    captain = ((sum(room_set) * K) - (sum(room_list))) // (K - 1)
    print(captain)
