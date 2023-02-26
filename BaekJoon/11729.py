n = int(input())

cnt = 0


def move(n, start, end):
    global cnt
    cnt += 1
    print(start, end)


def hanoi(n, start, end, sub):
    if n == 1:
        move(1, start, end)
        return

    hanoi(n-1, start, sub, end)
    move(n, start, end)
    hanoi(n-1, sub, end, start)


print(2**n - 1)
hanoi(n, 1, 3, 2)
