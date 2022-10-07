#Binary Search
def b_s(l2, low, high, a):
    if high >= low:
        mid = (high + low) // 2
        if mid == a:
            return mid
        elif mid > a:
            return b_s(l2, low, mid + 1, a)
        elif mid < a:
            return b_s(l2, mid - 1, high, a)
    else:
        return -1
#l2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Enter search value(" + str(l2[0]) + " - " + str(l2[-1]) + "): ")
a = int(input())
low, high = int(l2[0]), int(l2[-1])
result = b_s(l2, low, high, a)
if result != -1:
    print("The value exists.")
else:
	print("The value doesn't exists.")