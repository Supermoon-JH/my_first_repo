n = int(input())

for _ in range(n):
    score = list(map(int, input().split()))
    num = int(score[0])
    score.pop(0)

    result = 0

    mean = sum(score) / num
    for i in range(num):
        if score[i] > mean:
            result += 1

    print(f"{result / num * 100:.3f}%")
