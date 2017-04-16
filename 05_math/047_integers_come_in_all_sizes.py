"""
Integers in Python can be as big as the bytes in your machine's memory.
There is no limit in size as there is: 2**31 - 1(c++ int) or  2**63 - 1(C++ long long int).

As we know, the result of a**b grows really fast with increasing b.

Let's do some calculations on very large integers.
"""
a, b, c, d = list(map(int, [input() for _ in range(4)]))
print(a ** b + c ** d)
