#!/usr/bin/env python3


# collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter


def calculate_revenue(stock, orders):
    stock = Counter(stock)
    revenue = 0

    for shoe, price in orders:
        quantity = stock.get(shoe)
        if quantity:
            stock[shoe] = quantity - 1
            revenue += price

    print(revenue)


if __name__ == '__main__':
    X = int(input())
    stock = list(map(int, input().split()))

    N = int(input())
    orders = []
    for _ in range(N):
        size, price = map(int, input().split())
        orders.append((size, price))

    calculate_revenue(stock, orders)
