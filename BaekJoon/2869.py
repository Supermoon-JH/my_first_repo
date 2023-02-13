import math

a, b, c = map(int, input().split())

print(math.ceil((c-b) / (a-b)))

#a * day - b * day-1 >= c
# (a-b)day + b >= c
#day >= c-b / a-b
