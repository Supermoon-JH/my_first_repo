num = int(input())
star = ""
for i in range(num):
    for j in range(i+1):
        star += "*"
    star += "\n"
print(star)
