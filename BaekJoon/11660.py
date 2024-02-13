import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = l[i - 1][j - 1] + dp[i][j - 1] + \
            dp[i - 1][j] - dp[i - 1][j - 1]

for _ in range(m):
    a, b, c, d = map(int, input().split())
    print(dp[c][d] - dp[c][b - 1] - dp[a - 1][d] + dp[a - 1][b - 1])
