#!/usr/bin/env python
#coding:utf-8



#插入
arr = [4,3,5,2,6,10,9,22,7]
len1 = len(arr)
for i in range(len1):
    for j in range(1,len1):
        num1 = j
        if arr[num1-1] < arr[j]:
            arr[num1-1],arr[j]=arr[j],arr[num1-1]
print arr


