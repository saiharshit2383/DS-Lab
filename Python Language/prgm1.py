#Linear Search
def linear_Search(l1, n, a):
    for i in range(0, n):
        if (l1[i] == a):
            return i
    res = -1
    return res
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = int(input("Enter search value(" + str(l1[0]) + " - " + str(l1[-1]) + "): "))
n = len(l1)
res = linear_Search(l1, n, a)

if res == -1:
    print("Element not found.")
else:
    print("Element found at position: " + str(res + 1))