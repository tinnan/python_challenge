"""
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
"""
from itertools import permutations

S, k = input().split()
for p in sorted(permutations(S, int(k))):
    print(''.join(p))
