l = []

for i in range(5):
    l.append(int(input()))

new = sorted(l)

print(int(sum(l)/5))
print(new[2])
