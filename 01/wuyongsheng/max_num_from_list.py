# encoding:utf-8
# Desc:一个序列[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
# 求这个list的最大的两个值
# max_num_from_list.py

arr = [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111,
       22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]
max_num1 = 0
max_num2 = 0
for num in arr:
    if max_num1 < num:
        max_num1 = num
    for val in arr:
        if max_num2 < val and val < max_num1:
            max_num2 = val
print "list的最大两个值:max_num1 = %s, max_num2 = %s" % (max_num1, max_num2)
