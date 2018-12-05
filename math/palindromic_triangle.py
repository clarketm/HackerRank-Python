#!/usr/bin/env python3

# Triangle Quest 2
# https://www.hackerrank.com/challenges/triangle-quest-2/problem

if __name__ == "__main__":
    N = int(input())

    # Using `list concatenation` and `one sequence`
    # for i in range(1, N + 1):
    #     seq = range(1, i + 1)
    #     prefix = list(map(str, seq))
    #     suffix = list(map(str, seq[-2::-1]))
    #     print(''.join(prefix + suffix))

    # Using `list concatenation` and `two sequences`
    for i in range(1, N + 1):
        prefix = list(map(str, range(1, i)))
        suffix = list(map(str, range(i, 0, -1)))
        print("".join(prefix + suffix))

    # Using `iterable unpacking` and `one sequence`
    # for i in range(1, N + 1):
    #     seq = range(1, i + 1)
    #     prefix = map(str, seq)
    #     suffix = map(str, seq[-2::-1])
    #     print(''.join([*prefix, *suffix]))

    # Using `iterable unpacking` and `two sequences`
    # for i in range(1, N + 1):
    #     seq = range(1, i + 1)
    #     prefix = map(str, range(1, i))
    #     suffix = map(str, range(i, 0, -1))
    #     print(''.join([*prefix, *suffix]))

    # Two-liner (using `sep`)
    # for i in range(1, int(input()) + 1):
    #     print(*[*map(str, range(1, i)), *map(str, range(i, 0, -1))], sep='')

    # Two-liner (using `join`)
    # for i in range(1, int(input()) + 1):
    #     print(''.join([*map(str, range(1, i)), *map(str, range(i, 0, -1))]))

    # Two-liner (using `pure mathematical approach`)
    # for i in range(1, int(input()) + 1):
    #     print(((10 ** i) // 9) ** 2)
    #     # =~ print(100 ** i // 81)

    # One-liner (using `join`)
    # print(*[''.join([*map(str, range(1, i)), *map(str, range(i, 0, -1))]) for i in range(1, int(input()) + 1)], sep='\n')

    # One-liner (using `string repetition`)
    # print(*[int('1' * i) ** 2 for i in range(1, int(input()) + 1)], sep='\n')

    # One-liner (using `pure mathematical approach`)
    # print(*[((10 ** i) // 9) ** 2 for i in range(1, int(input()) + 1)], sep='\n')
