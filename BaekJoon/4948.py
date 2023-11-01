def prime(x):
    for i in range(2, int(x ** 0.5) + 1):    # 소수 판별 시 n의 제곱근까지만 탐색
        if x % i == 0:
            return False
    return True


while True:
    n = int(input())

    if n == 0:
        break

    answer = 0
    if n == 1:
        answer = 1
        print(answer)
        continue

    for i in range(n + 1, 2 * n):
        if prime(i):
            answer += 1

    print(answer)
