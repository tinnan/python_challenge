"""
A postal code P must be a number in the range of (100000 - 999999).
A postal code P must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words,
an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Your task is to validate whether P is a valid postal code or not.
"""
import re

valid_code = r'^[1-9]\d{5}$'  # 100000 - 999999
alt_repeat = r'(.)(?=.\1)'    # finding alternating repetitive

code = input()
alt = re.findall(alt_repeat, code)
alt_check = alt is None or (alt is not None and len(alt) <= 1)
print(all([bool(re.match(valid_code, code)), alt_check]))
