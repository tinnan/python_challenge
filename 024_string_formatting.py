"""
Given an integer, n, print the following values for each integer i from 1 to n:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n.
Each value should be space-padded to match the width of the binary value of 1.
"""


def print_formatted(number):
    # first, find length of binary of n
    length = len('{:b}'.format(number))
    # print decimal, octal, capitalized, hexadecimal
    for i in range(1, number + 1):
        print('{: >{width}d} {: >{width}o} {: >{width}X} {: >{width}b}'.format(i, i, i, i, width=length))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
