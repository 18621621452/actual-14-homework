#!/bin/env python
# encoding:utf-8
arr= [4,3,1,100,11,345]
length=len(arr)
#从第二个值开始循环
for i in range(1,length):
	#判断当前值比前一个值小则继续
	if arr[i] < arr[i-1]:
		temp = arr[i]
		j = i
		#依次跟前面的值比较并插入并将大的值往后移，直到J小于0
		while j > 0 and arr[j-1] > temp:
			arr[j],arr[j-1] = arr[j-1],temp
			j -=1
			print arr
print arr
