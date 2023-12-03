from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
final = []

while q:
    index, num = q.popleft()
    final.append(index + 1)

    if num > 0:
        q.rotate(-(num - 1))
    else:
        q.rotate(-(num))

print(' '.join(map(str, final)))
