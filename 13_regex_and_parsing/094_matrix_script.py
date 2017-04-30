"""
Neo has a complex matrix script. The matrix script is a N X M grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script,
then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
"""
import re

N, M = list(map(int, input().split()))
matrix = [list(input()) for _ in range(N)]
# matrix -> zip -> list -> map.. join tuples to array of text -> join array to a string
text = ''.join(list(map(lambda x: ''.join(list(x)), list(zip(*matrix)))))
# regex finding 1 or more symbols (plus spaces) sandwiched between alphanumerics and substitute them with single space
print(re.sub(r'(?<=[a-zA-Z0-9])[!@#$%&\s]+(?=[a-zA-Z0-9])', lambda m: ' ', text))
