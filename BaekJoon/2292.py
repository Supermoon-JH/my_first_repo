n = int(input())

cnt = 1
result = 0

while cnt < n:
    result += 1
    cnt += 6 * result

print(result+1)
