import sys
input = sys.stdin.readline

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
res = 2147000000


def dfs(depth, idx):
    global res
    if depth == n // 2:
        a = 0
        b = 0
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    a += score[i][j]
                elif not visited[i] and not visited[j]:
                    b += score[i][j]
        res = min(res, abs(a - b))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, idx + 1)
            visited[i] = False


dfs(0, 0)
print(res)
