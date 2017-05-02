"""
You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.
"""
import numpy as np

N, M = list(map(int, input().split()))
a = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.transpose(a))
print(a.flatten())
