"""
There is a horizontal row of n cubes. The length of each cube is given.
You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube(i) is
on top of cube(j) then sideLength(j) >= sideLength(i).

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
"""
from collections import deque
for _ in range(int(input())):
    C = int(input())
    H = deque(list(map(int, input().split())))
    result = -1
    preceding_cube = 0
    for i in range(C):
        try:
            left = H.popleft()
        except IndexError:
            left = 0
        try:
            right = H.pop()
        except IndexError:
            right = 0
        if i > 0 and (left > preceding_cube or right > preceding_cube):
            result = False  # Both side must passes the check, else it will not be able to continue eventually
            break
        lesser = min(('appendleft', left), ('append', right), key=lambda x: x[1])
        getattr(H, lesser[0])(lesser[1])  # Use the greater one and push the lesser one back in
        if i == C - 1:
            result = True  # Has reached the last cube of horizontal row
        preceding_cube = max(left, right)
    print('Yes' if result else 'No')
