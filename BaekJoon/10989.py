import sys

n = int(sys.stdin.readline())

count = [0] * 10001

for i in range(n):
    x = int(sys.stdin.readline())
    count[x] += 1

for i in range(10001):
    for j in range(count[i]):
        print(i)
