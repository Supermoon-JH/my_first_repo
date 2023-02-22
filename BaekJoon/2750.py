n = int(input())
l = []


# def quick_sort(arr):
#    if len(arr) <= 1:
#        return arr
#
#    pivot, tail = arr[0], arr[1:]
#
#    left = [i for i in tail if i <= pivot]
#    right = [i for i in tail if i > pivot]
#
#    left = [] if left is None else left
#    right = [] if right is None else right
#
#    return quick_sort(left) + [pivot] + quick_sort(right)


for i in range(n):
    l.append(int(input()))

l = sorted(l)

for i in range(n):
    print(l[i])
