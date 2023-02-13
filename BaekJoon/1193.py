a = int(input())

b = 1
c = 2

while b < a:
    b += c
    if b >= a:
        b -= c
        break
    c += 1

# print(a, b, c)
# c번째줄 a-b번째 숫자
if a == 1:
    print("1/1")
elif c % 2 == 1:
    print(f"{c-(a-b-1)}/{a-b}")
else:
    print(f"{a-b}/{c-(a-b-1)}")
