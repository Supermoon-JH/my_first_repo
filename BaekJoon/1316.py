n = int(input())

result = n

for _ in range(n):
    l = []
    a = input()
    s = 0
    for i in range(len(a)):
        l.append(a[i])
    for i in range(len(a)-1):
        if l[i] != l[i+1]:
            for j in range(i+2, len(a)):
                if l[i] == l[j]:
                    s = 1
    if s == 1:
        result -= 1

print(result)
