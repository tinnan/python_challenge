"""
Given 2 timestamps, print the absolute difference (in seconds) between them.

Timestamps are given in the format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. See the sample below for details.
"""
import datetime as dt
f = '%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):
    d1 = dt.datetime.strptime(input(), f)
    d2 = dt.datetime.strptime(input(), f)
    print(round(abs(d1 - d2).total_seconds()))
