lst = [4, 8, 1, 5, 7]
print('[1] 삽입 정렬 전: ', lst)

for i in range(1, len(lst)):
    while i > 0 and lst[i-1] > lst[i]:
        lst[i-1], lst[i] = lst[i], lst[i-1]
        i -= 1

print('[2] 삽입 정렬 후: ', lst)
