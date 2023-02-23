n = int(input())

l = list(map(int, input().split()))

s = set(l)

s = sorted(s)

d = {x: i for i, x in enumerate(s)}

for i in l:
    print(d[i], end=' ')
