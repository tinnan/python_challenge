"""
Let's dive into the interesting topic of regular expressions! You are given some input,
and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7, 8 or 9.
"""
import re
phone_pattern = re.compile(r'^[789][0-9]{9}$')

for _ in range(int(input())):
    print('YES' if bool(phone_pattern.match(input())) else 'NO')
