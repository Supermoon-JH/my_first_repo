a = int(input())
b = int(input())


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


l = []
for j in range(a, b+1):
    if is_prime(j) == True:
        l.append(j)

if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))
