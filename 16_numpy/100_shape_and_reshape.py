"""
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
"""
import numpy as np

a = np.array(list(map(int, input().split()))).reshape(3, 3)
print(a)
