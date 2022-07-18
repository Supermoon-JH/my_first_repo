a, b = map(int, input().split())
c = int(input())

d = c // 60
e = c % 60
hr = a + d
mnt = b + e

if mnt >= 60:
    if hr + 1 >= 24:
        print(hr - 23, mnt - 60)
    else:
        print(hr + 1, mnt - 60)
else:
    if hr >= 24:
        print(hr - 24, mnt)
    else:
        print(hr, mnt)
