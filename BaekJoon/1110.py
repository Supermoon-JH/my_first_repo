a = int(input())

num = a
# print(a)

i = 0

while 1:
    b = num // 10 + num % 10
    num = num % 10 * 10 + b % 10

    i += 1
    if num == a:
        break

print(i)
