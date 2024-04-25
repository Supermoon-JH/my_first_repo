import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))

low, high = 1, max(L)

while low <= high:
    mid = (low + high) // 2

    s = 0
    for i in L:
        if mid < i:
            s += (i - mid)

    if s < M:
        high = mid - 1
    else:
        low = mid + 1

print(high)
