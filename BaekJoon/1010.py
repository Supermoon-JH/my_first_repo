import sys
input = sys.stdin.readline

n = int(input())


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)


for _ in range(n):
    n, m = map(int, input().split())
    print(int(fact(m) / (fact(n) * fact(m-n))))
