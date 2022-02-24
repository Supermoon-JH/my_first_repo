scores = input('학생 5명의 수학 점수를 입력하세요: ').split()

sum = 0
scores_num = len(scores)

for i in range(0, scores_num):
    if int(scores[i]) >= 60:
        sum += int(scores[i])

print(f'학생 {scores_num}명의 입력 점수 중 60점 이상의 합계는? {sum}점 입니다.')
