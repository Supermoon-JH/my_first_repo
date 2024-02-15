import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))

time.sort()

a = 0
sum = 0

for i in time:
    sum += i
    a += sum

print(a)
