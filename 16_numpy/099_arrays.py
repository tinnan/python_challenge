"""
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
"""
import numpy as np

a = np.array(list(map(float, input().split())), float)[::-1]
print(a)
