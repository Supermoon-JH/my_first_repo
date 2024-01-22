import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
dp = [0] * n

dp[0] = l[0]
if n > 1:
    dp[1] = l[0] + l[1]

for i in range(2, n):
    dp[i] = max(dp[i-2] + l[i], dp[i-1], l[i] +
                l[i-1] + (dp[i-3] if i > 2 else 0))

print(dp[n-1])
