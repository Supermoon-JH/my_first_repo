num = int(input())

for _ in range(num):
    h, w, n = map(int, input().split())

    if n % h == 0:
        print(f"{h*100 + n//h}")
        # if n // h >= 10:
        #    print(f"{h}" + f"{(n//h)}")
        # else:
        #    print(f"{h}" + "0" + f"{(n//h)}")
    else:
        print(f"{n%h*100 + n//h + 1}")
        # if n // h >= 10:
        #    print(f"{n%h}" + f"{(n//h) + 1}")
        # else:
        #    print(f"{n%h}" + "0" + f"{(n//h)+1}")
