num = int(input())

for _ in range(num):
    k = int(input())
    n = int(input())

    f0 = [i for i in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            f0[i] += f0[i-1]

    print(f0[n-1])
    # 0: 1 2 3 4
    # 1: 1 1+2 1+2+3 1+2+3+4
    # 2: 1 1+1+2 1+1+2+1+2+3 1+1+2+1+2+3+1+2+3+4
    # 3: 1 1+1+1+2
