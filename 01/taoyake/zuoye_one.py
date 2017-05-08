#!/usr/bin/python
#-*- coding:utf-8 -*-
#定义一个序列为List
List=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#设置Max1的默认值是0
Max1=0
#设置Max2的默认值是0
Max2=0

#第一次使用for循环来遍历List这个列表，查找出来第一个最大值
for j in List:
    if j > Max1:
        Max1 = j
    #第二次使用for循环来遍历List这个列表，找出来比max1小的第二个最大值
    for k in List:
        if Max2 < k and k < Max1:
            Max2 = k
print '第一个最大值是:',Max1
print '第二个最大值是:',Max2
