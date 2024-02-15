import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    l.append(tuple(map(int, input().split())))

l.sort(key=lambda x: (x[1], x[0]))

answer = 1
end = l[0][1]

for i in range(1, n):
    if l[i][0] >= end:
        answer += 1
        end = l[i][1]

print(answer)
