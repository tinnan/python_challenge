"""
You are given a valid XML document, and you have to print the maximum level of nesting in it.
Take the depth of the root as 0.
"""
import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    current_lvl = level + 1
    new_max = current_lvl + (1 if len(elem) > 0 else 0)
    if new_max > maxdepth:
        maxdepth = current_lvl
    for e in elem:
        depth(e, current_lvl)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
