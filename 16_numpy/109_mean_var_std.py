"""
You are given a 2-D array of size NxM.
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None
"""
import numpy as np

N, M = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.mean(A, axis=1))
print(np.var(A, axis=0))
print(np.std(A))
