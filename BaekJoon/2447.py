n = int(input())
arr = [[" " for _ in range(n)] for _ in range(n)]


def draw_star(n, x, y):
    if n == 1:
        arr[y][x] = "*"
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw_star(n // 3, x + j * (n // 3), y + i * (n // 3))


draw_star(n, 0, 0)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
