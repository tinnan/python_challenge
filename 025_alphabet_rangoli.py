"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Ex. Size = 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""
# unicode base
base = 97


def print_rangoli(size):
    line_size = 4*size - 3


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
