"""
You are given two values a and b.
Perform integer division and print a/b.
In the case of ZeroDivisionError or ValueError, print the error code.
"""
for _ in range(int(input())):
    try:
        a, b = list(map(int, input().split()))
        print(a//b)
    except Exception as e:
        print('Error Code:', e)
