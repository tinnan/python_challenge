"""
You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.

Note: Do not print data if data == '\n'.
"""
from html.parser import HTMLParser

class MyParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(*(data.split(sep='\n')), sep='\n')

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)

s = ''
for _ in range(int(input())):
    s += input().rstrip()
    s += '\n'
p = MyParser()
p.feed(s)
p.close()
