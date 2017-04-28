"""
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F. (1 2 3 4 5 6 7 8 9 0 A B C D E and F).
■ A-F letters can be lower case. (a b c d e and f are also valid digits).
"""
import re

hex_color = re.compile(r':?.(#([0-9A-Fa-f]{3}){1,2})')
for _ in range(int(input())):
    f = hex_color.finditer(input())
    for m in f:
        print(m.group(1))
