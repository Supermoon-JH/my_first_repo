import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().rstrip().split()))
spc = list(map(int, input().rstrip().split()))

ans = []


def back_tracking(depth, total, plus, minus, multiply, divide):
    if depth == n:
        ans.append(total)
        return

    if plus:
        back_tracking(depth + 1, total +
                      num[depth], plus - 1, minus, multiply, divide)
    if minus:
        back_tracking(depth + 1, total -
                      num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        back_tracking(depth + 1, total *
                      num[depth], plus, minus, multiply - 1, divide)
    if divide:
        back_tracking(
            depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


back_tracking(1, num[0], spc[0], spc[1], spc[2], spc[3])
print(max(ans))
print(min(ans))
