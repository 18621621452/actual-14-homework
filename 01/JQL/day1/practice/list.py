#!/usr/bin/env python
#coding:utf-8
#遍历一个序列，统计序列中js的出现次数
count = 0
li = ['c','js','python','css','js','html','node','js']
for i in li:
    if i == 'js':
        count += 1
print count
