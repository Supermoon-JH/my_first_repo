n = int(input())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


b = []
for i in range(n):
    b.append(int(input()))

c = []
for i in range(n-1):
    c.append(b[i+1] - b[i])

g = c[0]
for i in range(len(c)-1):
    g = gcd(g, c[i+1])

answer = 0
for i in c:
    answer += i // g - 1

print(answer)
