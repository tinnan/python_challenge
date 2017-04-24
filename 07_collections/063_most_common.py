"""
You are given a string S.
The string contains only lowercase English alphabet characters.

Your task is to find the top three most common characters in the string S.
"""
from collections import Counter
L = sorted(list(Counter(input()).items()), key=lambda x: (-x[1], x[0]))
for i in range(3):
    print('{} {}'.format(L[i][0], L[i][1]))
