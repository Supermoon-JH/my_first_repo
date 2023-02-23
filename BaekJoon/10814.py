n = int(input())
l = []

for i in range(n):
    a, b = input().split()
    l.append((int(a), b, i))

new = sorted(l, key=lambda i: (i[0], i[2]))

for i in new:
    print(i[0], i[1])
