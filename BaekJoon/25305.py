n, k = map(int, input().split())

score = list(map(int, input().split()))

new = (sorted(score))
print(new[-k])
