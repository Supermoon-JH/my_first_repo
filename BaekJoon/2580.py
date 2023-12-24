import sys
input = sys.stdin.readline

problem = []
blank = []

for i in range(9):
    problem.append(list(map(int, input().rstrip().split())))

for i in range(9):
    for j in range(9):
        if problem[i][j] == 0:
            blank.append((i, j))


def check_row(x, n):
    for i in range(9):
        if n == problem[x][i]:
            return False
    return True


def check_col(y, n):
    for i in range(9):
        if n == problem[i][y]:
            return False
    return True


def check_rec(x, y, n):
    index_x = x // 3 * 3
    index_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == problem[index_x + i][index_y + j]:
                return False
    return True


def sudoku(index):
    if index == len(blank):
        for i in range(9):
            print(*problem[i])
        exit(0)

    for i in range(1, 10):
        x = blank[index][0]
        y = blank[index][1]

        if check_row(x, i) and check_col(y, i) and check_rec(x, y, i):
            problem[x][y] = i
            sudoku(index + 1)
            problem[x][y] = 0


sudoku(0)
