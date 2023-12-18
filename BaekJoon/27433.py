import sys
input = sys.stdin.readline

n = int(input())


def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)


print(fact(n))
