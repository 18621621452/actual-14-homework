#!/usr/bin/env python
#coding:utf-8
#用户一直输入数字，如果没有输入任何值，终止程序，打印所有输入数字的平均值
sum1 = 0
num = 0
times = 0
while num !='':
    num = raw_input('please input your num:')
    if num !='':
        sum1 = sum1+int(num)
        times = times+1
print sum1*1.0/times

