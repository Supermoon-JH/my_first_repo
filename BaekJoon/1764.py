n, m = map(int, input().split())

s = set()
r = 0
l = []

for _ in range(n):
    s.add(input())

for i in range(m):
    a = input()
    if a in s:
        r += 1
        l.append(a)

new = sorted(l)

print(r)
for i in range(r):
    print(new[i])

#n, m = map(int, input().split())
#
#hear = set()
#speak = set()
#
# Read in the first list of strings
# for i in range(n):
#    name = input()
#    hear.add(name)
#
# Read in the second list of strings
# for i in range(m):
#    name = input()
#    speak.add(name)
#
# Find the strings that appear in both lists
#common = sorted(list(hear.intersection(speak)))
#
# Print the number of common strings and the strings themselves
# print(len(common))
# for name in common:
#    print(name)
