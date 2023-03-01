a = input()
r = set()
# 1 2 3 4 5 12 23 34 45 123 234 345 1234 2345 12345
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        b = a[i:j]
        r.add(b)

print(len(r))
