# Selection Sort
def s_s(array, size):
	for ind in range(size):
		min_index = ind
		for j in range(ind + 1, size):
			if array[j] < array[min_index]:
				min_index = j
		(array[ind], array[min_index]) = (array[min_index], array[ind])
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
s_s(arr, size)
print('Ascending Order by selection sort is:')
print(arr)
print('Descending Order by selection sort is:')
print(arr[::-1])