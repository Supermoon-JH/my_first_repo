n, m = map(int, input().split())


a = set(map(int, input().split()))
b = set(map(int, input().split()))


new1 = a - b
new2 = b - a
new3 = new1 | new2

print(len(new3))
