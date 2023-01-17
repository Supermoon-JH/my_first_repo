n = int(input())

for _ in range(n):
    a, b = input().split()
    a = int(a)
    c = ""
    for i in range(len(b)):
        c += b[i]*a
    print(c)
