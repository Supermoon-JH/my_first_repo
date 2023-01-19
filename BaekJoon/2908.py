a, b = map(str, input().split())

c = list(a)
d = list(b)
c[0], c[-1] = c[-1], c[0]
d[0], d[-1] = d[-1], d[0]

a = int(''.join(c))
b = int(''.join(d))

print(max(a, b))
