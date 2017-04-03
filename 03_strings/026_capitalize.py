"""
You are given a string S. Your task is to capitalize each word of S.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
"""


def capitalize(string):
    return ' '.join([s[0:1].upper() + s[1:].lower() for s in string.split(' ')])  # words as list

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
