# Insertion sort
def i_s(arr):
	for i in range(0, len(arr)):
		k = arr[i]
		j = i - 1
		while j >=0 and k < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = k
#arr = [12, 11, 13, 5, 6]
arr = [51, 6, 94, 82, 75, 1, 45, 0, 61, 50]
i_s(arr)
lst = []
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i])
print("In Ascending Order:", lst)
print("In Descending Order:", lst[::-1])