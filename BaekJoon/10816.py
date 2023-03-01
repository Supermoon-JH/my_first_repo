n = int(input())
l_n = list(map(int, input().split()))
m = int(input())
l_m = list(map(int, input().split()))

count = {}

for i in l_n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for j in l_m:
    if j in count:
        print(count[j], end=' ')
    else:
        print("0", end=' ')
