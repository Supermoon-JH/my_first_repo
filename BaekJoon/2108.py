n = int(input())
l = []


for i in range(n):
    x = int(input())
    l.append(x)


new = sorted(l)

d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

m = max(d.values())
new2 = [k for k, v in d.items() if v == m]
new3 = sorted(new2)

print(round(sum(l) / n))
print(new[n//2])
if len(new3) == 1:
    print(new3[0])
else:
    print(new3[1])
print(max(l) - min(l))
