num = int(input())

for _ in range(num):
    result = list(input())

    score = 0
    final_score = 0

    for i in result:
        if i == 'O':
            score += 1
            final_score += score
        else:
            score = 0
    print(final_score)
