"""
You are given a string S, containing , and/or . and 0-9 digits.
Your task is to re.split() all of the , and . symbols.
"""
import re
print(*[s for s in re.split(r'[.,]', input()) if s], sep='\n')
