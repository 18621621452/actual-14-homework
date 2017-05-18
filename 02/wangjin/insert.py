#!/usr/bin/python
#coding:utf8

arr1 = [10,9,8,7,6,5,4,3,2,1]

for i in range(1, len(arr1)):
    j = i - 1                         #定义一个变量j，利用j来对加入的对象在已排序好的队列中比较
    tem = 0                           #领用tem变量来对需要替换值的临时存储
    while j >= 0:
        if arr1[j + 1] < arr1[j]:     #第一次循环中的j+1就是外层循环中需要加入数
            tem = arr1[j]             #后面的循环是找这个新插入的数合适的位置。
            arr1[j] = arr1[j + 1]
            arr1[j + 1] = tem
        j -= 1


print arr1

#缩减版,利用python中的  a,b=b,a   来兑换值。
arr1 = [10,9,8,7,6,5,4,3,2,1]

for i in range(1, len(arr1)):
    j = i - 1
    while j >= 0:
        if arr1[j + 1] < arr1[j]:
            arr1[j],arr1[j + 1] = arr1[j + 1],arr1[j]
        j -= 1

print arr1
