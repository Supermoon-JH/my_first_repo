m, n = map(int, input().split())


def prime(x):
    for i in range(2, int(x ** 0.5) + 1):    # 소수 판별 시 n의 제곱근까지만 탐색
        if x % i == 0:
            return False
    return True


for i in range(m, n + 1):
    if i != 1 and prime(i):
        print(i)
