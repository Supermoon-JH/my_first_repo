n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

new = sorted(l)

for i in range(n):
    print(new[i])
