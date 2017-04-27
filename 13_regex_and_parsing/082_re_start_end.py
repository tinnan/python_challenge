"""
You are given a string S.
Your task is to find the indices of the start and end of string k in S.
"""
import re

S, k = input(), r'(?=(' + input() + '))'
m = re.finditer(k, S)
l = ['({}, {})'.format(t.start(1), t.end(1)-1) for t in m]
if len(l) > 0:
    print(*l, sep='\n')
else:
    print('(-1, -1)')
