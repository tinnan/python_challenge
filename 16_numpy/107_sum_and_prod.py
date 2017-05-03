"""
You are given a 2-D array with dimensions NxM.
Your task is to perform the sum tool over axis 0 and then find the product of that result.
"""
import numpy as np

N, M = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.product(np.sum(A, axis=0)))
