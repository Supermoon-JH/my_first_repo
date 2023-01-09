n = int(input())

number = list(map(int, input().split()))
k = int(input())

a = 0

for i in range(n):
    if number[i] == k:
        a += 1

print(a)
