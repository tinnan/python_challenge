"""
You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then,
apply the map function and a lambda expression to cube each fibonacci number and print the list.
"""
cube = lambda x: x**3


def fibonacci(n):
    if n < 3:
        return list(range(n))
    fib = [0, 1]
    for i in range(2, n):
        fib.append(sum(fib[i-2:i]))
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
