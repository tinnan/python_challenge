"""
You are given a 2-D array with dimensions NxM.
Your task is to perform the min function over axis 1 and then find the max of that.
"""
import numpy as np

N, M = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.max(np.min(A, axis=1)))
