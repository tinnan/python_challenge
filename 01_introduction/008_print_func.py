"""
Read an integer N.

Without using any string methods, try to print the following:
123...N
"""

if __name__ == '__main__':
    n = int(input())
    [print(i + 1, end="") for i in range(n)]
