import sys
input = sys.stdin.readline

l = input().rstrip().split('-')
new = []

for i in l:
    sum = 0
    a = i.split('+')
    for j in a:
        sum += int(j)
    new.append(sum)

answer = new[0]
for i in range(1, len(new)):
    answer -= new[i]

print(answer)
