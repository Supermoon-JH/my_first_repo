# 스택을 구현하고 스택을 테스트합니다.
# 리스트를 이용한 스택 구현
stack = []          # 비어있는 리스트를 생성

# 무한 반복문을 이용해서 계속 명령어를 받을 수 있도록 합니다.
while True:
    cmds = input(">> ").split()

    # quit 명령어가 들어오면 반목문을 나간다.
    if cmds[0] == 'quit':
        break

    # 스택 명령어들 처리
    if cmds[0] == 'add':
        stack.append(cmds[1])
    elif cmds[0] == 'pop':
        print(stack.pop())
    elif cmds[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print("Empty")
    elif cmds[0] == 'empty':
        print(len(stack) == 0)
