"""
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.
"""
from collections import OrderedDict
D = OrderedDict()
for _ in range(int(input())):
    W = input()
    D[W] = D[W] + 1 if W in D else 1
print(len(D.values()))
print(' '.join(map(str, D.values())))
