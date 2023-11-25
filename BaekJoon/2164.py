from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])
for i in range(n):
    q.append(i + 1)

if n == 1:
    print(1)
for _ in range(n-1):
    q.popleft()
    if len(q) == 1:
        print(q[0])
        break
    else:
        a = q.popleft()
        q.append(a)
