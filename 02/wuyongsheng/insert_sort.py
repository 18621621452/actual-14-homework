# encoding:utf-8
# 插入排序

arr = [71, 60, 49, 11, 24, 3, 66]
# 列表长度
length = len(arr)
# 从列表第2个元素，依次与已排序列表中第1个元素比较
for i in range(1, length):
    for j in range(i, 0, -1):
        # print i, j
        # 待排序的元素比列表中已排序的元素小，那么将列表中元素依次从右向左移动位置，存放新插入的元素
        if arr[j - 1] > arr[j]:
            # print arr[j - 1], arr[j]
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            print arr
