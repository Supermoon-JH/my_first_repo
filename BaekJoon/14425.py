n, m = map(int, input().split())
l = []
s = set()
r = 0

for i in range(n):
    s.add(input())

for i in range(m):
    if input() in s:
        r += 1

print(r)
