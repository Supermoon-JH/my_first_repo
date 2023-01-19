a = input()
b = 0


for i in range(len(a)):
    if a[i] == " ":
        b += 1
if a[0] != " ":
    b += 1
if a[-1] == " ":
    b -= 1


print(b)
