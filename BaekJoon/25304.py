total = int(input())
count = int(input())
c = 0

for i in range(count):
    a, b = map(int, input().split())
    c += a * b

if c == total:
    print("Yes")
else:
    print("No")
