import sys
input = sys.stdin.readline

k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]

high = max(l)
low = 1

while low <= high:
    mid = (low + high) // 2
    a = 0

    for i in l:
        a += i // mid

    if a < n:
        high = mid - 1
    else:
        low = mid + 1


print(high)
