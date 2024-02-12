import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

count = [0] * m
count[0] = 1

sum = 0
for i in l:
    sum = (sum + i) % m
    count[sum] += 1

answer = 0
for i in count:
    if i > 1:
        answer += i * (i - 1) // 2

print(answer)
