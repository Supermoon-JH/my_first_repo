count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    print(f"Case #{int(i+1)}: {int(a+b)}")
