import sys
input = sys.stdin.readline

m, n = map(int, input().split())
d = {}

for i in range(m):
    word = input().rstrip()
    if len(word) >= n:
        if word not in d:
            d[word] = 1
        elif word in d:
            d[word] += 1

sorted_items = sorted(d.items(), key=lambda item: (
    -item[1], -len(item[0]), item[0]))

for i in sorted_items:
    print(i[0])
