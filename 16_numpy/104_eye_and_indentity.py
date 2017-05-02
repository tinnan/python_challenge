"""
Your task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.
"""
import numpy as np

N, M = list(map(int, input().split()))
print(np.eye(N, M))
