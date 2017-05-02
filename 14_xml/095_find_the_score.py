"""
You are given a valid XML document, and you have to print its score. The score is calculated by the sum
of the score of each element. For any element, the score is equal to the number of attributes it has.
"""
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    s = 0
    for n in node:
        s += get_attr_number(n)
    return len(node.attrib) + s

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# ** When running this code, end the input with a Ctrl+D
