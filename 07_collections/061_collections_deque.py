"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
"""
from collections import deque
d = deque()
for _ in range(int(input())):
    line = input().split()
    cmd = line[0]
    if cmd == 'pop' or cmd == 'popleft':
        getattr(d, cmd)()
    else:
        getattr(d, cmd)(line[1])
print(' '.join(d))
