import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
w = 0
b = 0


def count(x, y, n):
    global w, b
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                count(x, y, n // 2)
                count(x, y + n // 2, n // 2)
                count(x + n // 2, y, n // 2)
                count(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        w += 1
    else:
        b += 1


count(0, 0, n)
print(w)
print(b)
