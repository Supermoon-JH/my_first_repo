import sys
input = sys.stdin.readline

n = int(input())
num = sorted(map(int, input().split()))
m = int(input())
new = map(int, input().split())


def find(data, x):
    s = 0
    e = len(data) - 1

    while s <= e:
        mid = (s + e) // 2
        if data[mid] == x:
            return True
        elif data[mid] < x:
            s = mid + 1
        else:
            e = mid - 1

    return False


for i in new:
    if find(num, i):
        print(1)
    else:
        print(0)
