import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
max_sum = current_sum = l[0]

for i in range(1, n):
    current_sum = max(l[i], current_sum + l[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
