"""
You are given a date. Your task is to find what the day is on that date.
"""
import calendar as c
m, d, y = list(map(int, input().split()))
print(c.day_name[c.weekday(y, m, d)].upper())
