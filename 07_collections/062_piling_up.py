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
    row = list(map(int, input().split()))
    result = -1
    for direction in range(2):  # Running check twice for each test case (popping left first, popping right first).
        H = deque(row)
        preceding_cube = H.pop() if direction == 0 else H.popleft()
        for i in range(1, C):
            left = H.popleft()
            right = H.pop()
            if cube > preceding_cube:
                result = False
                H.append(cube)  # Put it back
            if result != 1:
                cube = H.popleft()  # check left
                if cube > preceding_cube:
                    result = False
                    H.appendleft(cube)  # put it back


            if i == C - 1:
                result = True  # Has reached the last cube of horizontal row
            preceding_cube = cube
        if result:
            break
    print('Yes' if result else 'No')
