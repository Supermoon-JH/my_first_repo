#import sys
# sys.setrecursionlimit(10**9)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


n = int(input())
print(fact(n))
