"""
You are given a set A and N number of other sets. These N number of sets have to perform some
specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.
"""
a_count, A = int(input()), set(map(int, input().split()))
cmd_count = int(input())
for _ in range(cmd_count):
    cmd = input().split()[0]
    N = set(map(int, input().split()))
    A.__getattribute__(cmd)(N)

print(sum(A))
