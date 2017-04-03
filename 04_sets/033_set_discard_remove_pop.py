"""
You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.
"""

if __name__ == '__main__':
    set_size, s = int(input()), set(map(int, input().split()))
    for _ in range(int(input())):
        line = input().split()
        cmd = line[0]
        if cmd == 'pop':
            s.__getattribute__(cmd)()
        else:
            s.__getattribute__(cmd)(int(line[1]))
    print(sum(s))
