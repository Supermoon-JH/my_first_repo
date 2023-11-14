import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    l = []
    a = input()
    for j in a:
        if j == '(':
            l.append(j)
        elif j == ')':
            if l:
                l.pop()
            else:
                print('NO')
                break
    else:
        if not l:
            print('YES')
        else:
            print('NO')
