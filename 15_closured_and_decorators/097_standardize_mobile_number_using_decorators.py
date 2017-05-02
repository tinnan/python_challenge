"""
Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them
in the standard format shown below:

+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number.
Alternatively, there may not be any prefix at all.
"""
import re


def standardize(l):
    pattern = re.compile(r'(\d{5})(\d{5})$')
    return [' '.join(['+91', *pattern.search(p).groups()]) for p in l]


def wrapper(f):
    def fun(l):
        return f(standardize(l))

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
