"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. If it does not appear, print -1.
"""
from collections import defaultdict

n, m = list(map(int, input().split()))
''' Correct answer , but not a good solution as this challenge is focusing on utilization of Default Dict object.
N = []
for _ in range(n):
    N.append(input())  # collecting N words in A group.
Found = defaultdict(list)
for i in range(m):
    f_pos = 0  # index finding position.
    M = input()  # An m word in B group.
    while f_pos <= n-1:
        try:
            f = N.index(M, f_pos)
            Found[i].append(f + 1)
            f_pos = f + 1  # Set finding position for next scan.
        except ValueError:
            if f_pos == 0:
                Found[i].append(-1)  # Not found any.
            break
    print(' '.join(map(str, Found[i])))
'''
N_indices = defaultdict(list)
for i in range(n):
    N_indices[input()].append(i+1)  # Collect indices of N words.

for _ in range(m):
    M_word = input()
    print(' '.join(map(str, N_indices[M_word])) if M_word in N_indices else '-1')
