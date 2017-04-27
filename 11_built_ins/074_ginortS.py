"""
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

- All sorted lowercase letters are ahead of uppercase letters.
- All sorted uppercase letters are ahead of digits.
- All sorted odd digits are ahead of sorted even digits.

Note:
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0.
b) You can only use one sorted function in your code. A 0 score will be awarded for using sorted more than once.
"""


def key_f(str):
    # The idea is convert ASCII code to make new order.
    if str.isalpha():
        if str.islower():  # ASCII of lower chars start from 97
            return ord(str) - 97  # Reindex to 0-25
        else:  # ASCII of upper chars start from 65
            return ord(str) - 39  # Reindex to 26-51
    else:  # ASCII of numeric chars start from 48
        # Reindex to start from 52
        idx = ord(str) + 4
        if int(str) % 2 == 0:  # Even
            return idx + 10
        else:
            return idx

print(*sorted(input(), key=key_f), sep='')
