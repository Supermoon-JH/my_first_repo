n, m = map(int, input().split())

l = []
for i in range(n):
    l.append(input())

result = n * m

for i in range(n-7):
    for j in range(m-7):
        r1 = 0
        r2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if l[x][y] != "W":
                        r1 += 1
                    if l[x][y] != "B":
                        r2 += 1
                else:
                    if l[x][y] != "B":
                        r1 += 1
                    if l[x][y] != "W":
                        r2 += 1
        result = min(result, r1, r2)

print(result)
