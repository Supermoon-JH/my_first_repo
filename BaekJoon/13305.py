import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
answer = 0
now = price[0]

for i in range(len(dist)):
    if price[i] < now:
        answer += dist[i] * price[i]
        now = price[i]
    else:
        answer += dist[i] * now

print(answer)
