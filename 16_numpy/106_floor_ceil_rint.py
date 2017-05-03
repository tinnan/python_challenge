"""
You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of .
"""
import numpy as np

A = np.array(list(map(float, input().split())))
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
