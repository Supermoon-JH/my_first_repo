import sys
input = sys.stdin.readline

n, k = map(int, input().split())

l = []
for i in range(n):
    l.append(int(input()))

answer = 0
a = 1000000000
b = 0
while k != 0:
    for i in l:
        if i <= k:
            a = min(a, k // i)
            b = max(b, i)

    answer += a
    k %= b
    a = 1000000000
    b = 0

print(answer)
