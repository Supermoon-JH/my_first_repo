n, m = map(int, input().split())

l = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if l[i] + l[j] + l[k] > m:
                continue
            else:
                result = max(result, l[i] + l[j] + l[k])

print(result)
