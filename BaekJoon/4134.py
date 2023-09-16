n = int(input())

# 함수 안쓰면 시간 초과


def prime(x):
    for i in range(2, int(x ** 0.5) + 1):    # 소수 판별 시 n의 제곱근까지만 탐색
        if x % i == 0:
            return False
    return True


for i in range(n):
    a = int(input())

    while True:
        if a == 0 or a == 1:
            print(2)
            break

        if prime(a):
            print(a)
            break
        else:
            a += 1
