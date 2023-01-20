a = input()

b = list(a)
n = 0
i = 0

while i < len(b):
    if i == len(b)-1:
        n += 1
    elif b[i] == "c" and (b[i+1] == "=" or b[i+1] == "-"):
        n += 1
        i += 1
    elif b[i] == "d" and b[i+1] == "z":
        if i == len(b)-2:
            n += 1
        elif b[i+2] == "=":
            n += 1
            i += 2
        else:
            n += 1
    elif b[i] == "d" and b[i+1] == "-":
        n += 1
        i += 1
    elif (b[i] == "l" or b[i] == "n") and b[i+1] == "j":
        n += 1
        i += 1
    elif (b[i] == "s" or b[i] == "z") and b[i+1] == "=":
        n += 1
        i += 1
    else:
        n += 1
    i += 1

print(n)
