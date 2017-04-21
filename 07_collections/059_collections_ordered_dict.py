"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
"""
from collections import OrderedDict
Purchase = OrderedDict()
for _ in range(int(input())):
    I, P = input().rsplit(maxsplit=1)
    Purchase[I] = Purchase[I] + int(P) if I in Purchase else int(P)
for I in Purchase.items():
    print(' '.join([I[0], str(I[1])]))
