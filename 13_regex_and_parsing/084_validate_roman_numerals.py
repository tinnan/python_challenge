"""
You are given a string, and you have to validate whether it's a valid Roman numeral.
If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

M 1000
D 500
C 100
L 50
X 10
V 5
I 1

I can be placed before V or X.
X can be placed before L or C.
C can be placed before D or M.
"""
import re

print(bool(re.match(r'^M{,3}(CM|D|CD){,1}C{,3}(XC|L|XL){,1}X{,3}(IX|V|IV){,1}I{,3}$', input())))
