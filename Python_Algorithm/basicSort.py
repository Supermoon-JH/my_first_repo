import time
import random


def selectionSort(v):
    n = len(v)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if v[j] < v[m]:
                m = j
        v[m], v[i] = v[i], v[m]


def insertionSort(v):
    n = len(v)
    for i in range(1, n):
        last = i-1
        c = v[i]
        while last >= 0 and v[last] > c:
            v[last+1] = v[last]
            last -= 1
        v[last+1] = c


def bubbleSort(v):
    n = len(v)
    for i in range(1, n):
        isDirty = False
        for j in range(n-1):
            if v[i] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                isDirty = True
        if not isDirty:
            break


#v = [random.randrange(1000000) for _ in range(10000)]
v = [_ for _ in range(10000)]
v.append(0)

ts = time.time()
bubbleSort(v)
print(v[:10])
et = time.time() - ts
print(f"Elapsed time is {et*1000:.2f}ms")
