# Quick Sort Iterative
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return (i+1)

def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition(arr, l, h)
        if (p - 1) > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        elif (p + 1) < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [19, 15, 3, 45, 62, 12, 71, 45]
print("Given Array is: ")
print(arr)
n = len(arr)
quickSortIterative(arr, 0, n-1)
s_arr = []
print ("Sorted array is:")
for i in range(n):
    s_arr.append(arr[i])
print(s_arr)