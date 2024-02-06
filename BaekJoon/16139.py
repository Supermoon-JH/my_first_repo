import sys
input = sys.stdin.readline

s = input()
q = int(input())
dp = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    for j in range(26):
        if ord(s[i - 1]) - 97 == j:
            dp[i][j] = dp[i - 1][j] + 1
        else:
            dp[i][j] = dp[i - 1][j]

for _ in range(q):
    a, b, c = input().split()
    b, c = int(b), int(c)
    print(dp[c + 1][ord(a) - 97] - dp[b][ord(a) - 97])
