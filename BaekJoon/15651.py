n, m = map(int, input().split())
l = []


def per():
    if len(l) == m:
        print(*l)
        return

    for i in range(1, n+1):
        l.append(i)
        per()
        l.pop()


per()
