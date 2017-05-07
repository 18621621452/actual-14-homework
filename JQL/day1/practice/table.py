#!/usr/bin/env python
#coding:utf-8
#打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        if i == j:
            print "%s*%s=%s" %(i,j,i*j)
        else:
            print "%s*%s=%s"%(i,j,i*j),
