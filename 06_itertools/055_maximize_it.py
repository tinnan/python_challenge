"""
You are given a function f(X) = X^2.

You are also given K lists. The ith list consists of Ni elements.

You have to pick exactly one element from each list so that the equation below is maximized:

S = (f(X1) + f(X2) + ... + f(Xk))%M

Xi denotes the element picked from the ith list . Find the maximized value Smax obtained.

% denotes the modulo operator.
"""
from itertools import product


def compute(args):
    s = 0
    for a in args:
        s += a**2
    return s % M

K, M = list(map(int, input().split()))
C = list(product(*[map(int, input().split()[1:]) for _ in range(K)]))
print(max(map(compute, C)))
