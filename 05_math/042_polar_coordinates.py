"""
You are given a complex z. Your task is to convert it to polar coordinates.
"""
import cmath

C = complex(input())
print(abs(C))
print(cmath.phase(C))
