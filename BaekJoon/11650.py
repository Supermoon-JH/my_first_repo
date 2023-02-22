n = int(input())
l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append((a, b))

new = sorted(l)

for x, y in new:
    print(x, y)
