"""
You are given a text of  lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or
Both && and || should have a space " " on both sides.
"""
import re

text = ''
for _ in range(int(input())):
    text += input() + '\n'
print(re.sub(r'(?<= )(\|{2}|&{2})(?= )', lambda x: 'and' if x.group(1) == '&&' else 'or', text))
