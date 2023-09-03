a, b = map(int, input().split())
c, d = map(int, input().split())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result


e = lcm(b, d)

son = (a * (e // b) + c * (e // d))

g = gcd(e, son)

son = son // g
mom = e // g

print(son, mom)
