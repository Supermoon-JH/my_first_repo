a = input()
answer = []

for i in range(26):
    answer.append(-1)

for i in range(len(a)):
    if answer[(ord(a[i])-97)] != -1:
        continue
    answer[(ord(a[i])-97)] = i

print(*answer)
