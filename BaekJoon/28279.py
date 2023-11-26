from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    num = input().split()
    num = [int(i) for i in num]
    if len(num) == 1:
        a = num[0]
    else:
        a = num[0]
        b = num[1]

    if a == 1:
        q.appendleft(b)
    elif a == 2:
        q.append(b)
    elif a == 3:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif a == 4:
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif a == 5:
        print(len(q))
    elif a == 6:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a == 7:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif a == 8:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
