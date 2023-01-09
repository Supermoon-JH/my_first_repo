a, b = map(int, input().split())
number = list(map(int, input().split()))

ans = []
for i in range(a):
    if number[i] < b:
        ans.append(number[i])

print(*ans)
