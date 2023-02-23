n = int(input())

l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append((a, b))

new = sorted(l, key=lambda i: (i[1], i[0]))

for i in new:
    print(i[0], i[1])
