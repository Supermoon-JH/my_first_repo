num = int(input())

# for _ in range(num):
#     a, b = map(int, input().split())
#     for i in range(max(a, b), a * b + 1):
#         if i % a == 0 and i % b == 0:
#             print(i)
#             break


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result


for _ in range(num):
    a, b = map(int, input().split())
    print(lcm(a, b))
