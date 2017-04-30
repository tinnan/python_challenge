"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank.
He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex
so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers
4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers
42536258796157867       #17 digits in card number → Invalid
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
"""
import re

valid_digits = re.compile(r'^[456]\d{3}(-?\d{4}){3}$')
no_con_repeat = re.compile(r'(?!.*(\d)\1{3})')
no_con_repeat_w_hyph = re.compile(r'(?!.*(\d)(\1{2}-\1{1}|\1{1}-\1{2}|-\1{3}))')
filters = valid_digits, no_con_repeat, no_con_repeat_w_hyph

for _ in range(int(input())):
    cc = input()
    if all(bool(f.match(cc)) for f in filters):
        print('Valid')
    else:
        print('Invalid')
