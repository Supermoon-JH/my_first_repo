import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    a = int(input())
    if a != 0:
        l.append(a)
    else:
        l.pop()

print(sum(l))
