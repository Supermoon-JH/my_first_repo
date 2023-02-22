n = int(input())

l = []

for i in range(len(str(n))):
    l.append(str(n)[i])

new = sorted(l, reverse=True)

print(*new, sep='')
