"""
You are given one set A and a number of other sets, N.
Your job is to find whether set A is a strict superset of all the N sets.
Print True, if A is a strict superset of all of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
"""
A = set(map(int, input().split()))
for _ in range(int(input())):
    N = set(map(int, input().split()))
    if A & N != N or not A ^ N:
        print(False)
        exit()
print(True)
