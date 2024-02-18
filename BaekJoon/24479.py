import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, len(graph)):
    graph[i].sort(reverse=True)


def dfs(start):
    need_visit = []
    need_visit.append(start)
    visited = [-1] * (n + 1)
    result = [0] * (n + 1)
    cnt = 1

    while need_visit:
        node = need_visit.pop()
        if visited[node] == -1:
            visited[node] = 1
            need_visit.extend(graph[node])

            result[node] = cnt
            cnt += 1

    return result


result = dfs(r)

print(*result[1:], sep='\n')
