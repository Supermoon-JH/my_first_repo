import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
new = []
new.append(sum(l[:k]))

for i in range(n - k):
    new.append(new[i] - l[i] + l[i + k])

print(max(new))
