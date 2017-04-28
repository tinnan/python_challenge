"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

- It must contain at least 2 uppercase English alphabet characters.
- It must contain at least 3 digits (0 - 9).
- It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
- No character should repeat.
- There must be exactly 10 characters in a valid UID.
"""
import re

proper_char_len = r'^[a-zA-Z\d]{10}$'
repeat = r'(?!.*(.).*\1)'
least_2_upper = r'.*[A-Z].*[A-Z].*'
least_3_digit = r'.*\d.*\d.*\d.*'
filters = proper_char_len, repeat, least_2_upper, least_3_digit

for _ in range(int(input())):
    uid = input()
    if all(bool(re.match(f, uid)) for f in filters):
        print('Valid')
    else:
        print('Invalid')
