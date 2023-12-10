import sys
input = sys.stdin.readline

n, k = map(int, input().split())


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)


print(int(fact(n) / (fact(k) * fact(n - k))))
