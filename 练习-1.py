# 1.冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))

# q:冒泡排序的时间复杂度是多少？
# a:O(n^2)
