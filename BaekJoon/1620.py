n, m = map(int, input().split())

# 리스트로 풀면 시간 초과
#p = []
#
# for i in range(n):
#    p.append(input())
#
# for i in range(m):
#    a = input()
#    if str.isdigit(a) == True:
#        print(p[int(a)-1])
#    else:
#        print(p.index(a)+1)

name_to_num = {}
num_to_name = {}

for i in range(1, n+1):
    a = input()
    name_to_num[a] = i
    num_to_name[i] = a

for i in range(m):
    b = input()
    if str.isdigit(b):
        print(num_to_name[int(b)])
    else:
        print(name_to_num[b])
