# 후위 연산자 식 계산하기

# stack 생성
stack = []

expr = input("수식: ").split()

for e in expr:
    # 연산자인지 아닌지 검사
    if e == '+' or e == '-' or e == '*' or e == '/':
        # 연산자 처리
        b = stack.pop()
        a = stack.pop()
        if e == '+':
            r = a+b
        elif e == '-':
            r = a-b
        elif e == '*':
            r = a*b
        elif e == '/':
            r = a/b
        stack.append(r)
    else:
        stack.append(float(e))

print(stack[0])
