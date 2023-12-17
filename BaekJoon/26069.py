n = int(input())
dance = ['ChongChong']

for _ in range(n):
    a, b = input().split()
    if a in dance:
        if b not in dance:
            dance.append(b)
    elif b in dance:
        if a not in dance:
            dance.append(a)

print(len(dance))
