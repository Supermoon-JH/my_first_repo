import sys
input = sys.stdin.readline


def kant(x, n):
    if n == 1:
        return
    for i in range(x + n // 3, x + (n // 3) * 2):
        s[i] = ' '
    kant(x, n // 3)
    kant(x + (n // 3) * 2, n // 3)


while True:
    try:
        n = int(input())
        s = ['-'] * 3 ** n
        kant(0, 3 ** n)
        print(''.join(s))
    except:
        break
