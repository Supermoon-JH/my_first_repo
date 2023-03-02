n, m = map(int, input().split())


def com(l, s):
    if len(l) == m:
        print(*l)
        return

    for i in s:
        if i in l:
            continue
        if l and i < l[-1]:
            continue

        com(l + [i], s - {i})


com([], set(range(1, n+1)))
