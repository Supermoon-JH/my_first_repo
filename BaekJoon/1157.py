a = input()
n = []

for _ in range(26):
    n.append(0)

for i in range(len(a)):
    if 65 <= ord(a[i]) <= 90:
        n[ord(a[i])-65] += 1
    else:
        n[ord(a[i])-97] += 1

num = 0
for i in range(26):
    if n[i] == max(n):
        num += 1

if num > 1:
    print("?")
else:
    print(chr(n.index(max(n))+65))
