import sys
input = sys.stdin.readline

n = int(input())

final = 0
chess = [0] * n


def confirm(x):
    for i in range(x):
        if chess[i] == chess[x] or abs(chess[x] - chess[i]) == abs(x - i):
            return False

    return True


def n_queen(x):
    global final

    if x == n:
        final += 1
        return
    else:
        for i in range(n):
            chess[x] = i
            if confirm(x):
                n_queen(x + 1)


n_queen(0)
print(final)
