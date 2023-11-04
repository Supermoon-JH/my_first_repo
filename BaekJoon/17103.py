import math

n = int(input())


prime = [False, False] + [True] * 999999

for i in range(2, 1000001):
    if prime[i]:
        for j in range(2 * i, 1000001, i):
            prime[j] = False


for _ in range(n):
    a = int(input())
    answer = 0
    for i in range(2, a // 2 + 1):
        if prime[i] and prime[a - i]:
            answer += 1

    print(answer)
