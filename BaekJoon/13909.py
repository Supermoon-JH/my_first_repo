import math
n = int(input())


def window(n):
    window = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            if window[j] == 0:
                window[j] = 1
            elif window[j] == 1:
                window[j] = 0

    print(window.count(1))


print(int(math.sqrt(n)))
