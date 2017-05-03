"""
You are given two arrays (A & B) of dimensions NxM.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Divide (A / B)
Mod (A % B)
Power (A ** B)
"""
import numpy as np

N, M = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
