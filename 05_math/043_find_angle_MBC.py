"""
ABC is a right triangle, 90 degree at B.
Therefore, angle of ABC = 90 degree.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find angle of MBC (angle 0 degree, as shown in the figure) in degrees.
"""
import math

AB, BC = int(input()), int(input())
print(str(round(math.degrees(math.atan2(AB, BC)))) + '\u00b0')
