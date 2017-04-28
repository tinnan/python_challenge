"""
You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.
"""
from html.parser import HTMLParser


class MyParser(HTMLParser):

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_starttag(self, tag, attrs):
        # check and print attribute list.
        print(tag)
        for a in attrs:
            print('-> {} > {}'.format(a[0], a[1]))

s = ''
for _ in range(int(input())):
    s += input()
    s += '\n'
p = MyParser()
p.feed(s)
p.close()
