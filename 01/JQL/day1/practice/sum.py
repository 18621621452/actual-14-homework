#!/usr/bin/env python
#coding:utf8
#让用户一直输入数字，如果输入的是0或者回车，终止程序，打印所有数字之和
count = 0
isContinue = True
while isContinue:
    num = raw_input('input your number:')
    if not num or num == 0:
        isContinue = False
    else:
        count = count+int(num)
print 'count is %s' %count
