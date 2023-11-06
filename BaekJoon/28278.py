import sys
input = sys.stdin.readline

n = int(input())
l = []


for i in range(n):
    num = list(map(int, input().split()))
    a = num[0]

    if a == 1:
        l.append(num[1])
    elif a == 2:
        if len(l) != 0:
            print(l.pop())
        else:
            print(-1)
    elif a == 3:
        print(len(l))
    elif a == 4:
        if len(l) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(l) != 0:
            print(l[-1])
        else:
            print(-1)
