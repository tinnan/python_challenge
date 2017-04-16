"""
You are given a two lists A and B. Your task is to compute their cartesian product AxB.
"""
from itertools import product

A, B = [list(map(int, input().split())) for _ in range(2)]
print(' '.join(['({}, {})'.format(*t) for t in product(A, B)]))
