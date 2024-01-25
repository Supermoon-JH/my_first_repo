import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

dp_i = [1] * n
dp_d = [1] * n
new = []

for i in range(1, n):
    for j in range(i):
        if l[i] > l[j] and dp_i[i] < dp_i[j] + 1:
            dp_i[i] = dp_i[j] + 1

for i in reversed(range(n - 1)):
    for j in reversed(range(i, n)):
        if l[i] > l[j] and dp_d[i] < dp_d[j] + 1:
            dp_d[i] = dp_d[j] + 1

for i in range(n):
    new.append(dp_i[i] + dp_d[i] - 1)

print(max(new))
