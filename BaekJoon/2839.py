s = int(input())
a = 0

while s >= 0:
    if s % 5 == 0:
        a += s // 5
        print(a)
        break

    s -= 3
    a += 1

else:
    print(-1)
