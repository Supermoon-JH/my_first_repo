n = int(input())
numbers = list(map(int, input().split()))
a = 0
b = 0

for i in numbers:
    if i == 2:
        a += 1
    elif i > 2:
        for j in range(2, i):
            if i % j == 0:
                b = 1
        if b == 0:
            a += 1
    b = 0
print(a)
