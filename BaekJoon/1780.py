import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

minus = 0
zero = 0
plus = 0


def paper(x, y, n):
    global zero, minus, plus
    value = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if value != graph[i][j]:
                value = -2

    if value == -2:
        n = n // 3
        paper(x, y, n)
        paper(x, y + n, n)
        paper(x, y + 2 * n, n)
        paper(x + n, y, n)
        paper(x + 2*n, y, n)
        paper(x + n, y + n, n)
        paper(x + n, y + 2*n, n)
        paper(x + 2*n, y + n, n)
        paper(x + 2*n, y + 2*n, n)

    elif value == -1:
        minus += 1
    elif value == 0:
        zero += 1
    elif value == 1:
        plus += 1


paper(0, 0, n)

print(minus)
print(zero)
print(plus)
