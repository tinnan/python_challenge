"""
You are given data in a tabular format. The data contains N rows, and each row contains M space separated elements.

You can imagine the M items to be different attributes, (like height, weight, energy, etc.) and each of the N rows as
an instance or a sample.

Your task is to sort the table on the Kth attribute and print the final resulting table.

Note: If two attributes are the same for different rows, print the row that appeared first in the input.
"""
N, M = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for i in sorted(L, key=lambda x: x[K]):
    print(*i)
