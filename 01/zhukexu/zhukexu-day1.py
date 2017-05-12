#/usr/bin/env python
#coding:utf-8
#作业
#一个序列[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#求这个list的最大的两个值
list1 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#定义初始值
num1 = 0
num2 = 0
for i in list1:
    if num1 < i:
        num1 = i
#如果有两个同样的最大值
    elif num1 == i:
        num2 = num1
for j in list1:
    if j < num1 and j > num2:
        num2 = j

print num1,num2
