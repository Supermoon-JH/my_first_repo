n, m = map(int, input().split())

l = []


def per(s):
    if len(l) == m:
        print(*l)
        return

    for i in range(s, n+1):
        l.append(i)
        per(i)
        l.pop()


per(1)
