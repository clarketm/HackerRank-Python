#!/usr/bin/env python3

# Lists
# https://www.hackerrank.com/challenges/python-lists/problem


def main(N):
    list = []

    while N > 0:
        i = input().split()

        if i[0] == 'insert':
            list.insert(int(i[1]), int(i[2]))
        elif i[0] == 'remove':
            list.remove(int(i[1]))
        elif i[0] == 'append':
            list.append(int(i[1]))
        elif i[0] == 'sort':
            list.sort()
        elif i[0] == 'reverse':
            list.reverse()
        elif i[0] == 'pop':
            list.pop()
        elif i[0] == 'print':
            print(list)

        N -= 1


if __name__ == '__main__':
    N = int(input())
    main(N)
