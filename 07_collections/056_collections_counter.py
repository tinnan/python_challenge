"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""
from collections import Counter

X = int(input())  # Number of shoes.
Shoes = Counter(list(map(int, input().split())))  # All shoes in the shop.
Earned = 0
for _ in range(int(input())):
    S, P = list(map(int, input().split()))  # Size and price.
    if S in Shoes and Shoes[S] > 0:
        Earned += P
        Shoes.subtract([S])  # Remove 1 shoes from the stock.
print(Earned)
