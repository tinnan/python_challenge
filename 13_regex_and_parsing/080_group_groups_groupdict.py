"""
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right)
that has consecutive repetitions.
"""
import re
se = re.search(r'([a-zA-Z0-9])\1+', input())
print(se.group(1) if bool(se) else '-1')
