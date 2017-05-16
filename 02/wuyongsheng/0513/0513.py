# encoding:utf-8

# list 切片
my_list = [1, 2, 3, 'hello', 'world', True, False, [7, 8, 9]]
print my_list[0]
print my_list[3]
print my_list[6]
print my_list[7]
print my_list[7][1]
print my_list[-1]
print my_list[-5]

# list 中 in 操作
arr = ['hello', 'world', 'python']
for name in arr:
    print name
print 'hello' in arr
print 'reboot' in arr
print len(arr)

# 模拟in操作
name = raw_input("input your name: ")
for num in arr:
    if num == name:
        print "True"
    else:
        print "False"

arr = ['hello', 'world', 'python']
is_in_arr = True
for name in arr:
    if 'hello1' == name:
        is_in_arr = True
        break
print is_in_arr


arr = ['hello', 'world', 'python']
del arr[0]
print arr
new_arr = ['!', '@', '.']
print arr + new_arr
arr[0] = 'reboot'
print arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print arr[2:5]
print arr[2:]
print arr[:5]
print arr[:]
print arr[::-1]
print arr[::2]
print arr[::]

print arr[5:2:-1]
print arr[::2]
# list 切片
#[start:end:step]
# step:
#    正数，从左向右取值
#    负数，从右向左取值
#    没有，默认从左向右取值
print arr
print arr[2:2]
arr[2:2] = ['xxx', '99', '!']  # 在第2个位置插入
print arr
arr[2:5] = ['111', '222']  # 删除2~5之间的值、替换
print arr
arr[5:2:-1] = ['w', 'e']
print arr

arr = [1, 2, 3]
arr.append(4)
print arr
print arr.count(2)
print arr

# 冒泡排序
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# 注意点: len(arr) - 1,意思，最后一个元素无法比较，因为
# 已经和倒数第2位比较过，故需要总长度减1
for j in range(len(arr) - 1): # 第一层循环控制排序的次数
    for i in range(len(arr) - 1): 第二层循环实现相邻元素值之间的位置交换
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print arr

# 对冒泡排序的优化:性能提高50% ，[3,2,1,4,5,6] 规避 4,5,6方法，排除排序的次数
for j in range(len(arr) - 1):  # 这层记录排序次数
    for i in range(len(arr) - j - 1):  # 加 -j 意思，规避已经排序好的顺序，这层记录左右值比较，交换位置
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print "%s exchanged num is %s vs %s" % (i, arr[i], arr[i + 1])
        print arr
print arr


# 选择排序
print "选择排序"
# print arr
# method1:
arr = [10, 7, 5, 3, 4, 9, 20, 19, 28, 14, 13, 99, 87, 76, 2]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            # print i,j,arr
print arr

# method2:
# 实现第1次选择排序交换,将最小值交换到最右边,被交换的值[10],存放在原来最小值[2]存放的位置
arr = [10, 7, 5, 3, 4, 9, 20, 19, 28, 14, 13, 99, 87, 76, 2]
length = len(arr)
min_num = 0
for i in range(length):
    if arr[i] < arr[min_num]:
        min_num = i
arr[0], arr[min_num] = arr[min_num], arr[0]
print arr

# 记录位置法
for j in range(length):
    min_num = j  # arr[j], 用于假设最小值的位置
    print "index is %s, %s" % (j, arr)
    for i in range(j + 1, length):
        if arr[i] < arr[min_num]:
            min_num = i  # 记录比较后，最小值的位置，用于下面值交换
    arr[j], arr[min_num] = arr[min_num], arr[j]  # 将指定的值，与比较后的值进行位置交换
print arr

# 排序算法 参考地址：
# http://blog.csdn.net/hijiankang/article/details/9207735


arr = [1, 2, 3]
arr.insert(1, 'hello')
print arr

arr = [5, 6, 7, 8]
print arr.pop()
print arr
print arr.pop(1)  # pop(param):列表的下标
print arr

arr.remove(6)  # remove()与del，pop之间区别
print arr

# arr = [80,90,100,10,5,21,31,45,60]
# # 取出列表中第5大的值
for i in range(5):  # 列表排序5次，倒取第5数取出 arr[-5]
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print arr[-5], arr

# 列表去重
arr = [1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12,
       3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]
res = []
for name in arr:
    if name not in res:
        res.append(name)
print res
# 最简单方法使用集合，因为集合有交集
new_arr = set(arr)
print list(new_arr)

# 取arr1和arr2相同的元素
# arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# arr2 = [2,1,3,2,43,234,454,452,234,14,21,14,4111]
# 取arr1和arr2 共同的元素
print list(set(arr1) & set(arr2))
