a, b = map(int, input().split())

if b - 45 >= 0:
    print(a, b - 45)
elif a == 0 and b - 45 < 0:
    print(23, b + 15)
elif b - 45 < 0:
    print(a - 1, b + 15)
