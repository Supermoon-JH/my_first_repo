a = str(input())


time = 0

for i in range(len(a)):
    if a[i] == "A" or a[i] == "B" or a[i] == "C":
        time += 3
    elif a[i] == "D" or a[i] == "E" or a[i] == "F":
        time += 4
    elif a[i] == "G" or a[i] == "H" or a[i] == "I":
        time += 5
    elif a[i] == "J" or a[i] == "K" or a[i] == "L":
        time += 6
    elif a[i] == "M" or a[i] == "N" or a[i] == "O":
        time += 7
    elif a[i] == "P" or a[i] == "Q" or a[i] == "R" or a[i] == "S":
        time += 8
    elif a[i] == "T" or a[i] == "U" or a[i] == "V":
        time += 9
    elif a[i] == "W" or a[i] == "X" or a[i] == "Y" or a[i] == "Z":
        time += 10

print(time)
