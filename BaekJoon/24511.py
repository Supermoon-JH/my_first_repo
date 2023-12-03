from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
type = list(map(int, input().split()))
q = list(map(int, input().split()))
n_2 = int(input())
num = list(map(int, input().split()))

final = deque()

for i in range(n):
    if type[i] == 0:
        final.appendleft(q[i])

for i in range(n_2):
    final.append(num[i])
    print(final.popleft(), end=' ')
