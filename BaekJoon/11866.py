from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = []
q = deque()

for i in range(n):
    q.append(i + 1)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    l.append(q.popleft())

print("<", end="")
for i in range(len(l) - 1):
    print(f"{l[i]},", end=" ")
print(l[-1], end="")
print(">")
