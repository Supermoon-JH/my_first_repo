import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]


def quad(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        quad(x, y, n)  # 왼쪽 위
        quad(x, y + n, n)  # 왼쪽 아래
        quad(x + n, y, n)  # 오른쪽 위
        quad(x + n, y + n, n)  # 오른쪽 아래
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


quad(0, 0, n)
