import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
sum = l[:]

for i in range(1, len(l)):
    sum[i] += sum[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    if i == j:
        print(l[i-1])
    elif i == 1:
        print(sum[j - 1])
    else:
        print(sum[j - 1] - sum[i - 2])
