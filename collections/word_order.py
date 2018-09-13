#!/usr/bin/env python3

# Word Order
# https://www.hackerrank.com/challenges/word-order/problem

# Using `Counter` and `OrderedDict`
# from collections import Counter, OrderedDict
#
# class OrderedCounter(Counter, OrderedDict):
#     pass
#
# if __name__ == '__main__':
#     n = int(input())
#
#     words = OrderedCounter(input() for word in range(n))
#     print(len(words))
#     print(*words.values())

# Using `OrderedDict`
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())

    words = OrderedDict()

    for _ in range(n):
        word = input()
        words[word] = words.get(word, 0) + 1

    print(len(words))
    print(*words.values())
