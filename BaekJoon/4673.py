num = []
for i in range(10000):
    num.append(i)


def self_num():
    for i in range(10000):
        if len(str(i)) == 1:
            num.remove(i*2)
        elif len(str(i)) == 2:
            num.remove(i + int(str(i)[0]) + int(str(i)[1]))
        elif len(str(i)) == 3:
            if i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) in num:
                num.remove(i + int(str(i)[0]) +
                           int(str(i)[1]) + int(str(i)[2]))
        else:
            if i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) in num:
                num.remove(i + int(str(i)[0]) + int(str(i)
                                                    [1]) + int(str(i)[2]) + int(str(i)[3]))


self_num()

for i in range(len(num)):
    print(num[i])
