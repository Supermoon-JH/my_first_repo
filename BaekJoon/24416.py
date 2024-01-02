import sys
input = sys.stdin.readline

n = int(input())
c = [0] * 50

a = 0
b = 0


def fib(x):
    global a
    if x == 1 or x == 2:
        a += 1
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def fibonacci(x):
    global b
    if x == 1 or x == 2:
        return 1
    if c[x] != 0:
        return c[x]
    b += 1
    c[x] = fibonacci(x-1) + fibonacci(x-2)
    return c[x]


fib(n)
fibonacci(n)
print(a, b)
