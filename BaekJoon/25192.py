import sys
input = sys.stdin.readline

n = int(input())
final = 0
d = {}

for i in range(n):
    message = input().replace('\n', '')
    if message == 'ENTER':
        for k, v in d.items():
            if v == 1:
                final += 1
        d = {}
    else:
        if message not in d:
            d[message] = 1

for k, v in d.items():
    if v == 1:
        final += 1

print(final)
