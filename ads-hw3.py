'''
#1
def heapify(a, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and a[l] > a[largest]:
        largest = l

    if r < n and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

A = [15, 3, 17, 10, 84, 19, 6, 22, 9]
n = len(A)

for i in range(n//2 - 1, -1, -1):
    heapify(A, n, i)

print("Max-Heap:", A)

A[0], A[n-1] = A[n-1], A[0]
heapify(A, n-1, 0)

print("After extract:", A)
'''

'''
#2
A = [15, 3, 17, 10, 84, 19, 6, 22, 9]

pivot = A[0]
left = []
right = []

for x in A[1:]:
    if x <= pivot:
        left.append(x)
    else:
        right.append(x)

result = left + [pivot] + right

print(result)
'''

'''
#3
def merge_sort(a):
    if len(a) <= 1:
        return a

    m = len(a)//2
    l = merge_sort(a[:m])
    r = merge_sort(a[m:])

    res = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i]); i+=1
        else:
            res.append(r[j]); j+=1

    return res + l[i:] + r[j:]


A = [15,3,17,10,84,19,6,22,9]
print(merge_sort(A))
'''

'''
#4
def merge_sort(a):
    if len(a) <= 1:
        return a

    m = len(a)//2
    left = merge_sort(a[:m])
    right = merge_sort(a[m:])

    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res + left[i:] + right[j:]

A = [15, 3, 17, 10, 84, 19, 6, 22, 9]

A = merge_sort(A)
print("Sorted array:", A)

target = 19

l = 0
r = len(A) - 1

while l <= r:
    mid = (l + r) // 2

    print("Low:", l, "High:", r, "Mid:", mid, "Value:", A[mid])

    if A[mid] == target:
        print("Found at index:", mid)
        break
    elif A[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
'''

'''
#5
A = [15, 3, 17, 10, 84, 19, 6, 22, 9]
target = 19

count = 0

for i in range(len(A)):
    count += 1
    if A[i] == target:
        print("Found at index:", i)
        break

print("Comparisons:", count)
'''

'''
#6
A = [15, 3, 17, 10, 84, 19, 6, 22, 9]

mn = A[0]
mx = A[0]

for x in A:
    if x < mn:
        mn = x
    if x > mx:
        mx = x

print("Min:", mn)
print("Max:", mx)
print("Range:", mx - mn)
'''
