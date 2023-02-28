n = int(input())
l = []
new = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    l.append((a, b))

for i in range(n):
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            new[i] += 1

print(* new)
