#!/bin/env python
# encoding: utf-8
#找出最大的两个数值
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
i=0
a=0
for num in arr:
	if num > i:
		i = num
for num in arr:
	if num > a and num < i:
		a = num
print 'The biggest number is %s'%(i)
print 'The second biggest number is %s'%(a)
