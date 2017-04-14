"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set , print True.
If set B is not a subset of set , print False.
"""
for _ in range(int(input())):
    A_cnt, A = int(input()), set(map(int, input().split()))
    B_cnt, B = int(input()), set(map(int, input().split()))
    print(True) if (B & A) == A else print(False)
