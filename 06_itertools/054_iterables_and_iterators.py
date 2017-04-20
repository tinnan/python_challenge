"""
You are given a list of N lowercase English letters. For a given integer K,
you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""
import itertools


def filter_func(t):  # predicate function for filtering combination with at least 1 occurrence of 'a'.
    for i in t:
        if N[i] == 'a':
            return True
    return False

L, N, K = int(input()), input().split(), int(input())
comp = list(itertools.combinations(list(range(L)), K))
prob = filter(filter_func, comp)
print(len(list(prob))/len(comp))
