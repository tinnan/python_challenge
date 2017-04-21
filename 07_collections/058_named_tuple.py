"""
Dr. John Wesley has a spreadsheet containing a list of student's ID, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
"""
from collections import namedtuple
N, Sheet = int(input()), namedtuple('Sheet', ' '.join(input().split()))
print('{:.2f}'.format(sum([int(Sheet(*input().split()).MARKS) for _ in range(N)]) / N))
