#!/usr/bin/env python3

# Collections.OrderedDict()
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

if __name__ == '__main__':
    N = int(input())

    inventory = OrderedDict()

    for _ in range(N):
        item_name, _, net_price = input().rpartition(' ')
        inventory[item_name] = inventory.get(item_name, 0) + int(net_price)

    for item_name, net_price in inventory.items():
        print(item_name, net_price)
