import sys
input = sys.stdin.readline

while True:
    s = input()
    l = []

    if s[0] == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            l.append(i)
        elif i == ')':
            if l and l[-1] == '(':
                l.pop()
            else:
                l.append(1)
                break
        elif i == ']':
            if l and l[-1] == '[':
                l.pop()
            else:
                l.append(1)
                break
    if l:
        print('no')
    else:
        print('yes')
