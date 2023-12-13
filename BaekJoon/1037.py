import sys
input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))

print(min(l) * max(l))
