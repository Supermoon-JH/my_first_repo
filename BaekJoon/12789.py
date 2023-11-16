import sys
input = sys.stdin.readline

n = int(input())
l = [int(i) for i in input().split()]

stack = []
food = 1

for i in l:
    if i == food:
        food += 1
    else:
        stack.append(i)

    while stack and stack[-1] == food:
        stack.pop()
        food += 1

if not stack:
    print("Nice")
else:
    print("Sad")
