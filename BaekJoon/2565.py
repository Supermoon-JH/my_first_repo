import sys
input = sys.stdin.readline

n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x: x[0])
r = [i[1] for i in l]

dp = [1] * n

for i in range(n):
    for j in range(i):
        if r[i] > r[j]:
            dp[i] = max(dp[i], dp[j] + 1)

answer = n - max(dp)
print(answer)
