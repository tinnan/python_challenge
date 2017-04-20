"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'x' with (X, c) in the string.
"""
from itertools import groupby

print(' '.join(['({}, {})'.format(len(list(g)), k) for k, g in groupby(input())]))
