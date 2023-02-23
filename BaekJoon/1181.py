n = int(input())

l = []

for i in range(n):
    l.append(input())

s = set(l)
new = list(s)
final = sorted(new, key=lambda i: (len(i), i))


for i in final:
    print(i)
