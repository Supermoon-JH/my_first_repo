n = int(input())


for i in range(1, n+1):
    d_sum = sum(map(int, str(i)))
    num = i + d_sum

    if num == n:
        print(i)
        break

    if i == n:
        print(0)
