a = int(input())
number = list(map(int, input().split()))

answer = [min(number), max(number)]
print(*answer)
