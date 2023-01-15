num = 0


def han(n):
    global num
    for i in range(1, n+1):
        if i < 100:
            num += 1
        elif i <= 1000:
            if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
                num += 1

    print(num)


han(int(input()))
