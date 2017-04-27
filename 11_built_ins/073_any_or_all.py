"""
You are given a space separated list of integers. If all the integers are positive,
then you need to check if any integer is a palindromic integer.
"""
N, L = int(input()), list(map(int, input().split()))
print(all([True if x >= 0 else False for x in L]) and any([True if str(x) == str(x)[::-1] else False for x in L]))
